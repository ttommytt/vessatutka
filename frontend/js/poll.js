			function checkBathroom() {
				$.get('/vessatutka/api/motion/')
				.done(function(data) {
					if(data.length && moment(data[0].timestamp).diff(moment()) < 30000) {
						$('.header').removeClass('free').addClass('reserved').html('Vessa on varattu');
					}
					else {
						$('.header').removeClass('reserved').addClass('free').html('Vessa on vapaa');
					}
					setTimeout(checkBathroom, 10000);
				})
				.fail(function() {
					setTimeout(checkBathroom, 10000);
				})

			}

			$( document ).ready(function() {
    			checkBathroom();
			});