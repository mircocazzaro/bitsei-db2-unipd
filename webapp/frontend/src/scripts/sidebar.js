function sidebarItems() {
    const sidebar = document.getElementById('sidebar');
    const sidebarContainer = sidebar.getElementsByClassName("position-sticky")

    const sidebarItems = [
        {
            id: 'home',
            href: '#query1',
            name: 'Query One',
            icon: 'feather feather-home'
        },
        {
            id: 'subItem2',
            href: '#query2',
            name: 'Query Two',
            icon: 'feather feather-home'
        },
        {
            id: 'subItem3',
            href: '#query3',
            name: 'Query Three',
            icon: 'feather feather-home'
        }
    ]

    // todo: fix icons

    const ul = document.createElement('ul');
    ul.classList.add('nav', 'flex-column');
    sidebarContainer[0].appendChild(ul);
    sidebarItems.forEach((item) => {
        const li = document.createElement('li');
        li.classList.add('nav-item');
        const a = document.createElement('a');
        a.classList.add('nav-link');
        a.setAttribute('href', item.href);

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.classList.add(...item.icon.split(' '));
        svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
        svg.setAttribute('width', '24');
        svg.setAttribute('height', '24');
        svg.setAttribute('viewBox', '0 0 24 24');
        svg.setAttribute('fill', 'none');
        svg.setAttribute('stroke', 'currentColor');
        svg.setAttribute('stroke-width', '2');
        svg.setAttribute('stroke-linecap', 'round');
        svg.setAttribute('stroke-linejoin', 'round');
        const path = document.createElement('path');
        path.setAttribute('d', 'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z');
        const polyline = document.createElement('polyline');
        polyline.setAttribute('points', '9 22 9 12 15 12 15 22');
        svg.appendChild(path);
        svg.appendChild(polyline);

        const span = document.createElement('span');
        span.classList.add('ml-2');
        span.innerText = item.name;
        a.appendChild(svg);
        a.appendChild(span);
        li.appendChild(a);
        ul.appendChild(li);
    });
}

window.addEventListener('load', sidebarItems, false);
