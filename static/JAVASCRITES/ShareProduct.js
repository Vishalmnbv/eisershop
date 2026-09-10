function shareProduct() {
    const url = window.location.href;
    const title = "{{ productview.producttitle|escapejs }}";
    if (navigator.share) {
        navigator.share({
            title: title,
            text: "Check out this product",
            url: url
        });
    } else {
        navigator.clipboard.writeText(url);
        alert("Product link copied successfully!");
    }
}