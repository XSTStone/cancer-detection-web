function goHome() {
    window.location.href="index"
}

function goAbout() {
    window.location.href="../index"
}

function uploadImg() {
    file.onclick()
}

function showExamples() {
    window.location.href="../index"
}

function retrainModel() {
    window.location.href="../index"
}

function login() {
    window.location.href="login"
}

function showHistory() {
    window.location.href="../index"
}

function showPicture() {
    window.location.href="../index"
}

function test() {
    window.location.href="detect/my_image.jpg"
}

// js 简要代码
const uploadFileEle = document.querySelector("#uploadFile");

const request = axios.create({
  baseURL: "http://localhost:3000/upload",
  timeout: 60000,
});

async function uploadFile() {
  if (!uploadFileEle.files.length) return;
  const file = uploadFileEle.files[0]; // 获取单个文件
  // 省略文件的校验过程，比如文件类型、大小校验
  upload({
    url: "/single",
    file,
  });
}

function upload({ url, file, fieldName = "file" }) {
  let formData = new FormData();
  formData.set(fieldName, file);
  request.post(url, formData, {
    // 监听上传进度
    onUploadProgress: function (progressEvent) {
      const percentCompleted = Math.round(
        (progressEvent.loaded * 100) / progressEvent.total
      );
      console.log(percentCompleted);
     },
  });
}