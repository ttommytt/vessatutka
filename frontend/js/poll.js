			function checkBathroom() {
				$.get('/vessatutka/api/motion/')
				.done(function(data) {
					if(data.length && moment(data[0].timestamp).diff(moment()) < 30000) {
						$('.header').html('Vessa on varattu');
					}
					else {
						$('.header').html('Vessa on vapaa');
					}
				})
				.fail(function() {
					setTimeout(checkBathroom, 10000);
				})

			}

			$( document ).ready(function() {
    			checkBathroom();
			});