// Initialize Google Map
function initMap() {
    const map = new google.maps.Map(document.getElementById("googleMap"), {
        center: { lat: 28.7041, lng: 77.1025 }, // Example: Delhi, India
        zoom: 8,
    });

    const heatmapData = [
        { location: new google.maps.LatLng(28.7041, 77.1025), weight: 2 },
        { location: new google.maps.LatLng(28.5355, 77.3910), weight: 3 },
    ];

    new google.maps.visualization.HeatmapLayer({
        data: heatmapData,
        map: map,
    });
}

// Call initMap when the window loads
window.onload = initMap;

// Handle Volunteer Registration
const volunteerForm = document.getElementById('volunteerForm');
const volunteerCount = document.getElementById('volunteer-count');

let volunteers = 0;

volunteerForm.addEventListener('submit', function (event) {
    event.preventDefault();
    volunteers++;
    volunteerCount.textContent = `${volunteers} volunteers available`;
    alert('Thank you for registering!');
});
