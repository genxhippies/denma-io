var $layer;

function init() {
    $layer = $('._layer').css({
		position: 'absolute',
		width: 300,
		border: '1px solid #666',
		backgroundColor: '#fff',
		opacity: 0.9,
		zIndex: 1000
	});
}

function getHtml(data) {
	var subTitle = '<h3>' + data.subtitle + ' </h3>';
	var pubDate = '<div>게시일: ' + data.publish_date + '</div>';
	var characters = '<div>등장 인물: ' + data.characters + '</div>';
	var url = '<div><a href="' + data.url + '" target="_new">보기</a></div>';

	return '<div>' + subTitle + pubDate + characters + url + '</div>';
}

function drawLayer(result) {
	$layer.html(getHtml(result));
}

function showLoading(offset) {
	$layer.html('<div>loading...</div>').css({
		left: offset.left - 60,
		top: offset.top + 18 + 4,
	}).show();
}