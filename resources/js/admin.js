var $layer;
var layerTemplate;
var scrollPosition = 0;

var $window = $(window);

$(document).ready(init);

function init() {
	$layer = $('._layer').css({
		position: 'absolute',
		opacity: 0.9,
		zIndex: 1000
	});

	$layer.on('click', function (e) {
		if ($(e.target).closest('.__close').length > 0) {
			$layer.hide();
			unfreezeBackground();
			e.preventDefault();
		}
	});

	layerTemplate = Handlebars.compile($('._layerTemplate').html());
}

function getHtml(data) {
	return layerTemplate({
		heading: data.subtitle,
		url: data.url
	});
}

function drawLayer(result) {
	var height = 0;
	
	if ($layer.is(':visible')) {
		$layer.html(getHtml(result));

		height = $layer.find('.__heading').outerHeight();

		$layer.find('.__toonContainer').css({
			height: $window.height() - (height + 30 + 2) // padding + border
		});
	}
}

function freezeBackground() {
	scrollPosition = $window.scrollTop();

	$('.__wrap').css({
		position: 'fixed',
		left: '0px',
		right: '0px',
		top: '0px',
		bottom: '0px',
		overflow: 'hidden',
		height: $window.height(),
	}).scrollTop(scrollPosition);

	$window.scrollTop(0);
}

function unfreezeBackground() {
	$('.__wrap').css({
		position: '',
		overflow: 'visible',
		height: 'auto'
	});

	$window.scrollTop(scrollPosition);
}
 
function showLoading() {
	var $output = $(layerTemplate({
		heading: '정보를 불러오고 있습니다.'
	}));

	$output.find('.__body').hide();

	freezeBackground();

	$layer.html($output.html()).css({
		left: 0,
		top: 0,
		width: '100%',
		height: '100%'
	}).show();
}