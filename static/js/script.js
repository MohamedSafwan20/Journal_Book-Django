loggedUser = document.querySelector(".logged-user").textContent;

if (loggedUser.length > 10)
  document.querySelector(".logged-user").textContent =
    loggedUser.slice(0, 10) + "...";

journalContents = document.querySelectorAll(".journal-content");

journalContents.forEach((journalContent) => {
  journalContentText = journalContent.textContent;

  if (journalContentText.length > 150)
    journalContent.textContent = journalContentText.slice(0, 150) + "...";
});
