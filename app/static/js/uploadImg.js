console.log("uploadImg is loaded.");

let images = [];
let currentIndex = 0;
let cropper = null;
let draggedIndex = null;

//  Dropzone配置
Dropzone.options.uploadForm = {
    maxFilesize: 5,
    acceptedFiles: 'image/*',
    autoProcessQueue: false,
    addRemoveLinks: false,
    previewsContainer: false,
    init: function() {
        this.on('addedfile', function(file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                images.unshift({
                    id: Date.now() + Math.random(),
                    src: e.target.result,
                    order: images.length
                });
                currentIndex = 0;
                updateUI();
            };
            reader.readAsDataURL(file);
        });
    }
};

//  UI更新
function updateUI() {
    updateMainImage();
    renderThumbnails();
    saveToSession();
}

// 今編集したい画像を選択
function updateMainImage() {
    const mainImage = document.getElementById('mainImage');
    const emptyState = document.getElementById('emptyState');
    
    if (images.length === 0) {
        mainImage.style.display = 'none';
        emptyState.style.display = 'flex';
        document.getElementById('prevBtn').disabled = true;
        document.getElementById('nextBtn').disabled = true;
    } else {
        mainImage.src = images[currentIndex].src;
        mainImage.style.display = 'block';
        emptyState.style.display = 'none';
        document.getElementById('prevBtn').disabled = false;
        document.getElementById('nextBtn').disabled = false;
    }
}

// 前の画像
function previousImage() {
    if (images.length > 0) {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateMainImage();
    }
}

// 後ろの画像
function nextImage() {
    if (images.length > 0) {
        currentIndex = (currentIndex + 1) % images.length;
        updateMainImage();
    }
}

// 画像削除
function deleteImage() {
    if (images.length === 0) return;
    images.splice(currentIndex, 1);
    if (currentIndex >= images.length && currentIndex > 0) {
        currentIndex--;
    }
    updateUI();
}

// 画像切り抜き
function editImage() {
    if (images.length === 0) return;
    
    const cropImage = document.getElementById('cropImage');
    cropImage.src = images[currentIndex].src;
    document.getElementById('cropModal').style.display = 'flex';
    
    if (cropper) cropper.destroy();
    
    setTimeout(() => {
        cropper = new Cropper(cropImage, {
            aspectRatio: NaN,
            viewMode: 1,
            autoCropArea: 0.8,
            responsive: true,
            guides: true,
            center: true,
            highlight: true,
            cropBoxMovable: true,
            cropBoxResizable: true
        });
    }, 100);
}

// 切り抜き保存
function saveCrop() {
    if (!cropper) return;
    images[currentIndex].src = cropper.getCroppedCanvas().toDataURL();
    cancelCrop();
    updateUI();
}

// 切り抜きキャンセル
function cancelCrop() {
    document.getElementById('cropModal').style.display = 'none';
    if (cropper) {
        cropper.destroy();
        cropper = null;
    }
}

// アップロード済み画像表示
function renderThumbnails() {
    const container = document.getElementById('thumbnailContainer');
    
    if (images.length === 0) {
        container.innerHTML = '<div class="text-gray-400 text-center w-full py-6">上傳した画像がここに表示されます</div>';
        return;
    }

    container.innerHTML = images.map((img, idx) => `
        <div 
            class="flex-shrink-0 group relative cursor-move"
            draggable="true"
            ondragstart="startDrag(event, ${idx})"
            ondragend="endDrag(event)"
            ondragover="allowDrop(event)"
            ondrop="dropOnThumbnail(event, ${idx})"
        >
            <img 
                src="${img.src}" 
                class="w-20 h-28 object-cover rounded-lg border-2 ${currentIndex === idx ? 'border-blue-500' : 'border-gray-300'} hover:border-blue-400 transition cursor-pointer"
                onclick="currentIndex = ${idx}; updateMainImage();"
            >
            <div class="absolute inset-0 rounded-lg bg-opacity-0 group-hover:bg-opacity-20 transition flex items-center justify-center">
                <span class="text-1xl text-white font-bold opacity-0 group-hover:opacity-100 text-stroke">Drag</span>
            </div>
        </div>
    `).join('');
}

// 並び順変える
function startDrag(e, idx) {
    draggedIndex = idx;
    e.dataTransfer.effectAllowed = 'move';
}

function endDrag(e) {
    draggedIndex = null;
}

function allowDrop(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
}

function dropOnThumbnail(e, targetIdx) {
    e.preventDefault();
    if (draggedIndex !== null && draggedIndex !== targetIdx) {
        [images[draggedIndex], images[targetIdx]] = [images[targetIdx], images[draggedIndex]];
        if (currentIndex === draggedIndex) currentIndex = targetIdx;
        else if (currentIndex === targetIdx) currentIndex = draggedIndex;
        updateUI();
    }
}

function handleDropOnThumbnails(e) {
    e.preventDefault();
}

// Session保存
function saveToSession() {
    sessionStorage.setItem('images', JSON.stringify(images));
}

// Session恢復
function loadFromSession() {
    const saved = sessionStorage.getItem('images');
    if (saved) images = JSON.parse(saved);
    updateUI();
}

// 初期化
loadFromSession();
