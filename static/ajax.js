//window.onload = function() {
	// setup the button click
//	document.getElementById("submit").onclick = function(data) {
//		postTrackingInput()
//	}

$(document).ready(function() {

	$('form').on('submit', function(event) {
		console.log("TEST: ", $('#trackingNoInput').val())
		$.ajax({
			data: { tracking_input: $('#trackingNoInput').val() },
			type: 'POST',
			url: '/get_track_url'
		})
		.done(function (data) {

			if (data.error) {
				//Show Error
				console.log('Some Error:', data)
			}
			else {
				//Redirect to "tracking_url"
				console.log('success!! DATA: ', data, 'URL: ', data['tracking_url'])
				window.location.replace(data['tracking_url'])
				//$('#main-iframe').attr('src', data['tracking_url']);
			}
		})
		.fail(function(error) {
			console.log('Ajax Error:', error)
			$('#order-not-found-error').show();
		})

		event.preventDefault()
	});
	
})