var $layer;

function init() {
	$layer = $('._layer').css({
		position: 'absolute',
		width: 616,
		border: '1px solid #666',
		backgroundColor: '#fff',
		opacity: 0.9,
		zIndex: 1000
	});
}

function drawLayer(result) {
	console.log('drawLayer');
}

function showLoading(offset) {
	$layer.html('<div>loading...</div>').css({
		left: 108,
		top: offset.top + 18 + 4,
	}).show();
}