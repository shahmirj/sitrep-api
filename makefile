
# Server PID File
SERVE_PIDFILE=".gunicorn.pid"

# Run all the tests required
test:
	@APPLICATION_ENV=testing python -m unittest discover -p "*Test.py" \
		-s tests/

# Install the python dataset
install:
	sudo pip install -r requirements.txt
install-travis:
	pip install -r requirements.txt

# Set the postdeploy to work
postdeploy:
	@python app/scripts/setup_database.py

# Start the process
serve-start:
	@gunicorn server:app -c config/gunicorn.py --log-file=- -p $(SERVE_PIDFILE) -D
	@if [ -f $(SERVE_PIDFILE) ]; then \
		echo -n "gunicorn is already running! "; \
	else \
		echo -n "Running gunicorn, "; \
	fi
	@echo "check log-file for details"

# Kill the process if it is running
serve-stop:
	@if [ -f $(SERVE_PIDFILE) ]; then \
		echo "Killing process:" $$(cat $(SERVE_PIDFILE)); \
	  kill $$(cat $(SERVE_PIDFILE)); \
	else \
		echo "Nothing to kill"; \
	fi

# Clean the data
clean:
	@find . -name "*.pyc" -delete
