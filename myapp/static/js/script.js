<script>
document.querySelector("form").addEventListener("submit", function(e) {
    let username = document.querySelector("input[name='username']").value;
    if(username.length < 3) {
        alert("Username must be at least 3 characters");
        e.preventDefault();
    }
});
</script>