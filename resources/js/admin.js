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
		url: data.url,
		starredCharacters: data.characters,
		allCharacters: data.allCharacters
	});
}

function parseData(data) {
	var characters = [];
	var allCharacters = [];

	_.each(data.characters.split(','), function (character) {
		if (character.length < 1) {
			return;
		}

		characters.push({
			name: $.trim(character)
		});
	});

	_.each(data.allCharacters.split(','), function (character) {
		if (character.length < 1) {
			return;
		}

		allCharacters.push({
			name: $.trim(character)
		});
	});

	data.characters = characters;
	data.allCharacters = allCharacters;

	return data;
}

function drawLayer(result) {
	var height = 0;

	if ($layer.is(':visible')) {

		result = parseData(result);

		$layer.html(getHtml(result));

		height = $layer.find('.__heading').outerHeight();

		$layer.find('.__toonContainer').css({
			height: $window.height() - (height + 30 + 2) // padding + border
		});

		presetCharacters();
		addEventHandlersOnChar();
	}
}

function presetCharacters() {
	var onList = [];
	var notOnList = [];

	$layer.find('.__charOnList').each(function (index, elem) {
		onList.push($(this).attr('data-name'));
	});

	$layer.find('.__charNotOnList').each(function (index, elem) {
		notOnList.push($(this).attr('data-name'));
	});

	_.each(onList, function (name) {
		setOnList(name);
	});
}

function setOnList(name) {
	$layer.find('.__charNotOnList[data-name="' + name + '"]')
			.removeClass('btn-primary')
			.addClass('btn-default')
			.prop('disabled', 'disabled');
}

function setNotOnList(name) {
	$layer.find('.__charNotOnList[data-name="' + name + '"]')
			.removeClass('btn-default')
			.addClass('btn-primary')
			.prop('disabled', '');
}

function addEventHandlersOnChar() {
	$layer.find('.__charOnList').on('click', function (e) {
		e.preventDefault();

		var $target = $(e.target);
		console.log($target.attr('data-name'));
	});

	$layer.find('.__charNotOnList').on('click', function (e) {
		e.preventDefault();

		var $target = $(e.target);
		console.log($target.attr('data-name'));
	});
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