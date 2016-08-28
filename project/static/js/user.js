$(function() {

	var width = 950,
		height = 450,
		$canvas, canvas, context;
	var datas = [{month: 3, receive: 10, give: 3}, {month: 4, receive: 1, give: 5},{month: 5, receive: 34, give: 10},{month: 6, receive: 20, give: 33},{month: 7, receive: 12, give: 0}];

	var myCanvas = {
		distance: 0, 
		spacing: 0,
		startX: 30,
		endX: 950,
		startY: 380,
		endY: 80,
		lineNum: 6,
		monthNum: 5,
		drawBackground: function() {
			myCanvas.pretreat(datas);
			var tempSpaceY = (this.startY-this.endY)/(this.lineNum - 1);
			for (var i = 0; i < this.lineNum; ++i) {
				if (i == 0) {
					context.strokeStyle = '#C0C0C0';
					context.lineWidth = 2;
					context.beginPath();
					context.moveTo(this.startX, this.startY);
					context.lineTo(this.endX, this.startY);
					context.stroke();
					context.strokeStyle = '#E8E8E8';
					context.lineWidth = 1;
					context.font = "18px microsoft yahei";
					context.fillStyle = "#ff851b";
					context.fillText(0, this.startX - 25, this.startY);
				} else {
					context.beginPath();
					context.moveTo(this.startX, this.startY-tempSpaceY*i);
					context.lineTo(this.endX, this.startY-tempSpaceY*i);
					context.stroke();
					context.fillText(this.spacing*i, this.startX - 25, this.startY-tempSpaceY*i);
				}
			}
		},
		translate: function(month, times) {

		},
		drawTitle: function(receive, give) {
			context.font = "20px microsoft yahei";
			var gradient = context.createLinearGradient(0, 0, 250, 0);
			gradient.addColorStop("0","blue");
			gradient.addColorStop("1.0","red");
			// 用渐变填色
			context.strokeStyle = gradient;
			context.strokeText("您已累计求助" + receive + "次，施助" + give +"次", 30, 30);
		},
		pretreat: function(data) {
			var temp = 0;
			for (var i = 0; i < data.length; ++i) {
				if (data[i].receive > temp) {
					temp = data[i].receive;
				}
			}
			this.distance = temp;
			this.spacing = Math.ceil(this.distance/this.lineNum);
		},
		drawNum: function() {
			var tempSpaceX = (this.startY-this.endY)/(this.lineNum - 1);
			for (var i = 0; i < this.lineNum; ++i) {
				if (i == 0) {
					context.strokeStyle = '#C0C0C0';
					context.lineWidth = 2;
					context.beginPath();
					context.moveTo(this.startX, this.startY);
					context.lineTo(this.endX, this.startY);
					context.stroke();
					context.strokeStyle = '#E8E8E8';
					context.lineWidth = 1;
				} else {
					context.beginPath();
					context.moveTo(this.startX, this.startY-tempSpaceY*i);
					context.lineTo(this.endX, this.startY-tempSpaceY*i);
					context.stroke();
				}
			}
		}
	}

	var initCanvas = function() {
		$canvas = $('.my-canvas');
		canvas = $canvas.get(0);
		$canvas.attr('width', width);
		$canvas.attr('height', height);
		context = canvas.getContext('2d');
		context.fillStyle = "white";
		context.fillRect(0, 0, width, height);
		myCanvas.drawBackground();
		myCanvas.drawTitle(10, 3);
	}

	var init = function() {
		$(window).on('scroll', watcher);
		$('.types').on('click', 'a', function() {
			$(this).addClass('active');
		});
		$('.types button').click(function() {
			$('.types button').removeClass('active');
			$(this).addClass('active');
		})
	}

	var fixTab = function() {
		$('.types').addClass('fixed');
	}

	var releaseTab = function() {
		$('.types').removeClass('fixed');
	}


	var changeTabPosition = function(top) {
		if (top >= 110) {
			$('.ghost').show();
			fixTab();
		} else {
			$('.ghost').hide();
			releaseTab();
		}
	}


	var watcher = function() {
		var top = $('body').scrollTop();
		changeTabPosition(top);
	}

	init();
	initCanvas();

});

