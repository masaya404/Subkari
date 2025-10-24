let currentImageIndex = 0;
        const images = [
            'https://via.placeholder.com/500x600/333/fff?text=Fur+Parker+1',
            'https://via.placeholder.com/500x600/444/fff?text=Fur+Parker+2',
            'https://via.placeholder.com/500x600/555/fff?text=Fur+Parker+3'
        ];
        
        function changeImage(direction) {
            currentImageIndex += direction;
            if (currentImageIndex < 0) currentImageIndex = images.length - 1;
            if (currentImageIndex >= images.length) currentImageIndex = 0;
            
            document.getElementById('mainImage').src = images[currentImageIndex];
            updateThumbnails();
        }

        function selectImage(index) {
            currentImageIndex = index;
            document.getElementById('mainImage').src = images[currentImageIndex];
            updateThumbnails();
        }

        function updateThumbnails() {
            const thumbnails = document.querySelectorAll('.thumbnail');
            thumbnails.forEach((thumb, index) => {
                thumb.classList.toggle('active', index === currentImageIndex);
            });
        }

        function switchTab(tabIndex) {
            const tabs = document.querySelectorAll('.tab');
            const contents = document.querySelectorAll('.tab-content');
            
            tabs.forEach((tab, index) => {
                tab.classList.toggle('active', index === tabIndex);
            });
            
            contents.forEach((content, index) => {
                content.classList.toggle('active', index === tabIndex);
            });
        }