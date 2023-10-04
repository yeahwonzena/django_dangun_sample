function previewImage(event) {
  let reader = new FileReader();
  reader.onload = function () {
    let output = document.getElementById("imagePreview");
    output.src = reader.result;
    output.classList.add("img-upload-fit");
  };
  reader.readAsDataURL(event.target.files[0]);
}

document.addEventListener("DOMContentLoaded", function () {
  let submitButton = document.getElementById("submit-button");
  let requiredInputs = document.querySelectorAll(
    "input[required], textarea[required]"
  );
  let form = document.querySelector(".write-box"); // 현재 폼을 선택합니다.

  submitButton.addEventListener("click", function (e) {
    let allFilled = true;
    requiredInputs.forEach((input) => {
      if (input.value === "") {
        allFilled = false;
      }
    });

    if (!allFilled) {
      e.preventDefault(); // 폼의 제출을 방지합니다.
      alert("모든 필드를 채워주세요."); // 알림을 표시합니다.
    }
  });
});
