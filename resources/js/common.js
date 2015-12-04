var $layer;
var layerTemplate;

function init() {
    $layer = $('._layer').css({
		position: 'absolute',
		width: 300,
		opacity: 0.9,
		zIndex: 1000
	});

	$layer.on('click', function (e) {
		if ($(e.target).closest('.__close').length > 0) {
			$layer.hide();
			e.preventDefault();
		}
	});

	layerTemplate = Handlebars.compile($('._layerTemplate').html());
}

function getHtml(data) {
	return layerTemplate({
		heading: data.subtitle,
		pubDate: data.publish_date,
		characters: data.characters,
		url: data.url
	});
}

function drawLayer(result) {
	if ($layer.is(':visible')) {
		$layer.html(getHtml(result));
	}
}

function showLoading(offset) {
	var $output = $(layerTemplate({
		heading: '정보를 불러오고 있습니다.'
	}));

	$output.find('.__body').hide();

	$layer.html($output.html()).css({
		left: offset.left - 60,
		top: offset.top + 18 + 4,
	}).show();
}