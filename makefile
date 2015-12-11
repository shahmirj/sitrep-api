
SERVE_PIDFILE=".gunicorn.pid"

test:
	@python -m unittest discover -p "Test*" -s tests/

# Install the python dataset
install:
	sudo pip install -r requirements.txt

# Start the process
serve-run:
	@gunicorn server:app -c config/gunicorn.py --log-file=- -p $(SERVE_PIDFILE) -D
	@if [ -f "$(SERVE_PIDFILE)" ]; then \
		echo -n "gunicorn is already running! "; \
	else \
		echo -n "Running gunicorn, "; \
	fi
	@echo "check log-file for details"

# Kill the process if it is running
serve-kill:
	@if [ -f "$(SERVE_PIDFILE)" ]; then \
		echo "Killing process:" $$(cat $(SERVE_PIDFILE)); \
	  kill $$(cat $(SERVE_PIDFILE)); \
	else \
		echo "Nothing to kill"; \
	fi
