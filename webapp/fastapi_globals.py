from collections.abc import Awaitable, Callable
from contextvars import ContextVar, copy_context
from typing import Any

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class Globals:
    __slots__ = ("_vars", "_defaults")

    _vars: dict[str, ContextVar]
    _defaults: dict[str, Any]

    def __init__(self) -> None:
        object.__setattr__(self, "_vars", {})
        object.__setattr__(self, "_defaults", {})

    def cleanup(self):
        """Clear all variables and free memory."""

        self._vars.clear()
        self._defaults.clear()
        del self._vars
        del self._defaults

    def set_default(self, name: str, default: Any) -> None:
        """Set a default value for a variable."""

        # Ignore if default is already set and is the same value
        if name in self._defaults and default is self._defaults[name]:
            return

        # Ensure we don't have a value set already - the default will have
        # no effect then
        if name in self._vars:
            raise RuntimeError(
                f"Cannot set default as variable {name} was already set",
            )

        # Set the default already!
        self._defaults[name] = default

    def _get_default_value(self, name: str) -> Any:
        """Get the default value for a variable."""

        default = self._defaults.get(name, None)

        # return default() if callable(default) else default
        return default

    def _ensure_var(self, name: str) -> None:
        """Ensure a ContextVar exists for a variable."""
        if name not in self._vars:
            default = self._get_default_value(name)
            self._vars[name] = ContextVar(f"globals:{name}", default=default)

    def __getattr__(self, name: str) -> Any:
        """Get the value of a variable."""

        self._ensure_var(name)
        return self._vars[name].get()

    def __setattr__(self, name: str, value: Any) -> None:
        """Set the value of a variable."""

        self._ensure_var(name)
        self._vars[name].set(value)


async def globals_middleware_dispatch(
        request: Request,
        call_next: Callable,
) -> Response:
    """Dispatch the request in a new context to allow globals to be used."""

    ctx = copy_context()

    def _call_next() -> Awaitable[Response]:
        return call_next(request)

    return await ctx.run(_call_next)


class GlobalsMiddleware(BaseHTTPMiddleware):  # noqa
    """Middleware to set up the globals context using globals_middleware_dispatch()."""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app, globals_middleware_dispatch)


g = Globals()
