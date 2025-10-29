   function startTimer() {
            let hours = 12, minutes = 59, seconds = 59;
            const timerEl = document.getElementById('timer');

            setInterval(() => {
                if (seconds > 0) {
                    seconds--;
                } else if (minutes > 0) {
                    minutes--;
                    seconds = 59;
                } else if (hours > 0) {
                    hours--;
                    minutes = 59;
                    seconds = 59;
                }

                const h = String(hours).padStart(2, '0');
                const m = String(minutes).padStart(2, '0');
                const s = String(seconds).padStart(2, '0');
                timerEl.textContent = `${h}:${m}:${s}`;
            }, 1000);
        }

        startTimer();