import os
import webbrowser

base_dir = r"C:\Users\admin\Desktop\fei_project"
sections = [
    {"id": "architecture-section", "folder": "architecture"},
    {"id": "illustration-section", "folder": "illustration"},
    {"id": "product-section", "folder": "product design"},
    {"id": "software-section", "folder": "Software"},
    {"id": "animation-section", "folder": "animation design"},
    {"id": "video-section", "folder": "videos"}
]

html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FEI Design Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollToPlugin.min.js"></script>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="logo">FEI Design</div>
        <ul class="nav-links">
            <li><a href="#home" data-hover="首页">Home</a></li>
            <li><a href="#portfolio" data-hover="作品集">Portfolio</a></li>
            <li><a href="#about" data-hover="关于我">About</a></li>
            <li><a href="#contact" data-hover="联系方式">Contact</a></li>
        </ul>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>FEI Design Portfolio</h1>
            <p>Exploring the fusion of modern and futuristic aesthetics</p>
        </div>
        <div class="hero-image" style="background-image: url('C:/Users/admin/Desktop/fei_project/architecture/architecture (1).png');"></div>
    </section>

    <!-- Highlights Section -->
    <section class="highlights">
        <h2>See the highlights of this website.</h2>
        <div class="highlight-grid">
"""

# 动态生成 Highlights 部分（保持不变）
for section in sections:
    folder_path = os.path.join(base_dir, section["folder"])
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and any(f.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.mp3', '.mp4'])]
        html_content += f"""
            <div class="highlight-item" onclick="scrollToSection('{section['id']}')">
                <div class="highlight-content">
                    <div class="grid-container">
        """
        for file in files:
            full_path = os.path.join(folder_path, file).replace("\\", "/")
            media_tag = f'<img src="{full_path}" alt="{file}" class="grid-item">' if any(file.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']) else f'<video muted loop class="grid-item"><source src="{full_path}" type="video/mp4"><source src="{full_path.replace(".mp4", ".webm")}" type="video/webm"><source src="{full_path.replace(".mp4", ".ogg")}" type="video/ogg"></video>'
            html_content += media_tag + "\n"
        html_content += f"""
                    </div>
                    <p class="zh-text">{section["id"].replace("-section", "").replace("-", " ").title()}</p>
                    <div class="en-text">{section["id"].replace("-section", "").replace("-", " ").title()}</div>
                </div>
            </div>
        """

html_content += """
        </div>
    </section>
"""

# 动态生成 Showcase 部分
for section in sections:
    folder_path = os.path.join(base_dir, section["folder"])
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and any(f.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.mp3', '.mp4'])]
        html_content += f"""
    <section id="{section['id']}" class="showcase-section">
        <h2>{section['id'].replace('-section', '').replace('-', ' ').title()} Showcase</h2>
        <div class="showcase-grid" data-path="{folder_path}">
"""
        for file in files:
            full_path = os.path.join(folder_path, file).replace("\\", "/")
            html_content += f'            <div class="showcase-item" data-file="{file}" onclick="openModal(\'{full_path}\', \'{file}\', {files.index(file)})" style="cursor: pointer;">\n'
            if any(file.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                html_content += f'                <img src="{full_path}" alt="{file}">\n'
            elif any(file.lower().endswith(ext) for ext in ['.mp4', '.mp3']):
                html_content += f'                <video autoplay muted loop><source src="{full_path}" type="video/{file.split(".")[-1].lower() if file.split(".")[-1].lower() in ['mp4', 'mp3'] else 'mp4'}"><source src="{full_path.replace(file.split(".")[-1], "webm")}" type="video/webm"><source src="{full_path.replace(file.split(".")[-1], "ogg")}" type="video/ogg"></video>\n'
            html_content += '            </div>\n'
        html_content += """
        </div>
    </section>
"""

html_content += """
    <!-- Modal for Enlarged View -->
    <div id="modal" class="modal" onclick="closeModal(event)">
        <span class="close">×</span>
        <div class="modal-content">
            <div id="modal-media"></div>
            <button id="prevBtn" onclick="changeMedia(-1, event)">❮</button>
            <button id="nextBtn" onclick="changeMedia(1, event)">❯</button>
        </div>
    </div>

    <!-- About Section (Placeholder) -->
    <section class="about">
        <h2>About Me</h2>
        <p>I am FEI, a designer passionate about blending modern and futuristic aesthetics across various disciplines.</p>
    </section>

    <script>
        // Parallax Effect
        window.addEventListener('scroll', () => {
            const scrollPosition = window.pageYOffset;
            const heroImage = document.querySelector('.hero-image');
            heroImage.style.backgroundPositionY = -scrollPosition * 0.3 + 'px';
        });

        // Scroll to Section Function
        function scrollToSection(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                document.querySelectorAll('.showcase-section').forEach(sec => {
                    sec.style.display = 'none';
                });
                section.style.display = 'block';
                setTimeout(() => {
                    gsap.to(window, {
                        duration: 1,
                        scrollTo: { y: section.offsetTop, autoKill: false },
                        ease: "power2.out"
                    });
                    ScrollTrigger.refresh();
                }, 100);
            }
        }

        // Highlight Hover Animation (Mark Clennon Style with Grid)
        gsap.utils.toArray('.highlight-item').forEach(item => {
            item.addEventListener('mouseenter', () => {
                gsap.to(item, { scale: 1.1, boxShadow: '0 15px 30px rgba(0, 0, 0, 0.4)', duration: 0.4, ease: "elastic.out(1, 0.3)" });
                gsap.to(item.querySelector('.highlight-content'), {
                    boxShadow: '0 0 40px rgba(255, 255, 255, 0.8), 0 0 60px rgba(255, 255, 255, 0.6)',
                    transform: 'translateY(-10px) rotate(2deg)',
                    duration: 0.4,
                    ease: "power2.out"
                });
                gsap.to(item.querySelectorAll('.grid-item'), { scale: 1.1, duration: 0.4, ease: "power2.out", stagger: 0.05 });
                gsap.to(item.querySelector('.zh-text'), { bottom: '2rem', opacity: 1, duration: 0.4, ease: "power2.out" });
            });
            item.addEventListener('mouseleave', () => {
                gsap.to(item, { scale: 1, boxShadow: '0 5px 10px rgba(0, 0, 0, 0.1)', duration: 0.4, ease: "power2.out" });
                gsap.to(item.querySelector('.highlight-content'), {
                    boxShadow: 'none',
                    transform: 'translateY(0) rotate(0deg)',
                    duration: 0.4,
                    ease: "power2.out"
                });
                gsap.to(item.querySelectorAll('.grid-item'), { scale: 1, duration: 0.4, ease: "power2.out", stagger: 0.05 });
                gsap.to(item.querySelector('.zh-text'), { bottom: '-50px', opacity: 0, duration: 0.4, ease: "power2.out" });
            });
            item.addEventListener('mousemove', (e) => {
                const rect = item.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                gsap.to(item.querySelector('.highlight-content'), {
                    rotationX: (-y / 20),
                    rotationY: (x / 20),
                    duration: 0.1
                });
            });
        });

        // Modal Functionality
        let currentIndex = 0;
        let currentPath = '';
        let files = [];

        function openModal(path, file, index) {
            currentPath = path.split('/').slice(0, -1).join('/'); // Extract directory path
            files = Array.from(document.querySelectorAll(`.showcase-grid[data-path="${currentPath}"] .showcase-item`)).map(item => item.getAttribute('data-file'));
            currentIndex = index;
            console.log("Opening modal for:", file, "at index:", currentIndex, "path:", currentPath, "files:", files); // Debug
            updateModal();
            document.getElementById('modal').style.display = 'block';
            gsap.from('#modal', { scale: 0.5, opacity: 0, duration: 0.5, ease: "back.out(1.7)" });
        }

        function closeModal(event) {
            if (event.target.className === 'modal') {
                gsap.to('#modal', { scale: 0.5, opacity: 0, duration: 0.3, ease: "power2.in", onComplete: () => {
                    document.getElementById('modal').style.display = 'none';
                }});
            }
        }

        function changeMedia(direction, event) {
            event.stopPropagation();
            currentIndex += direction;
            if (currentIndex < 0) currentIndex = files.length - 1;
            if (currentIndex >= files.length) currentIndex = 0;
            console.log("Changing to index:", currentIndex); // Debug
            updateModal(direction);
        }

        function updateModal(direction = 0) {
            const file = files[currentIndex];
            const fullPath = `${currentPath}/${file}`;
            const ext = file.split('.').pop().toLowerCase();
            const media = ['png', 'jpg', 'jpeg'].includes(ext) 
                ? `<img src="${fullPath}" alt="Enlarged ${file}" style="max-width: 100%; max-height: 100%;">`
                : `<video controls autoplay muted><source src="${fullPath}" type="video/mp4"><source src="${fullPath.replace('.mp4', '.webm')}" type="video/webm"><source src="${fullPath.replace('.mp4', '.ogg')}" type="video/ogg"></video>`;
            
            gsap.to('#modal-media', {
                opacity: 0,
                x: direction > 0 ? -100 : 100,
                filter: 'blur(10px)',
                duration: 0.3,
                ease: "power2.in",
                onComplete: () => {
                    document.getElementById('modal-media').innerHTML = media;
                    gsap.fromTo('#modal-media', {
                        opacity: 0,
                        x: direction > 0 ? 100 : -100,
                        filter: 'blur(10px)',
                        scale: 0.9
                    }, {
                        opacity: 1,
                        x: 0,
                        filter: 'blur(0px)',
                        scale: 1,
                        duration: 0.5,
                        ease: "power2.out"
                    });
                }
            });
        }

        // Dynamic Media Loading for Showcase
        document.querySelectorAll('.showcase-grid').forEach(grid => {
            const basePath = grid.getAttribute('data-path');
            grid.querySelectorAll('.showcase-item').forEach(item => {
                const fileName = item.getAttribute('data-file');
                const fullPath = `${basePath}/${fileName}`;
                const ext = fileName.split('.').pop().toLowerCase();

                if (['png', 'jpg', 'jpeg'].includes(ext)) {
                    item.innerHTML = `<img src="${fullPath}" alt="${grid.parentElement.querySelector('h2').textContent} ${item.querySelector('h3') ? item.querySelector('h3').textContent : ''}">`;
                } else if (['mp4', 'mp3'].includes(ext)) {
                    item.innerHTML = `<video autoplay muted loop><source src="${fullPath}" type="video/${ext === 'mp3' ? 'mpeg' : ext}"><source src="${fullPath.replace('.' + ext, '.webm')}" type="video/webm"><source src="${fullPath.replace('.' + ext, '.ogg')}" type="video/ogg"></video>`;
                }

                gsap.from(item, {
                    opacity: 0,
                    y: 50,
                    duration: 1,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: item,
                        start: "top 80%",
                        end: "bottom 20%",
                        toggleActions: "play none none none"
                    }
                });

                const media = item.querySelector('video') || item.querySelector('img');
                if (media) {
                    item.addEventListener('mouseenter', () => {
                        gsap.to(item, { transform: 'translateY(-5px)', duration: 0.3, ease: "power1.out" });
                        gsap.to(media, { scale: 1.05, duration: 0.3, ease: "power1.out" });
                    });
                    item.addEventListener('mouseleave', () => {
                        gsap.to(item, { transform: 'translateY(0)', duration: 0.3, ease: "power1.out" });
                        gsap.to(media, { scale: 1, duration: 0.3, ease: "power1.out" });
                    });
                }
            });
        });
    </script>
</body>
</html>"""

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

webbrowser.open(f'file:///{os.path.abspath(os.path.join(base_dir, "index.html")).replace("\\", "/")}')

print("HTML file generated and opened successfully!")