VIRTUALENV = $(shell which virtualenv)

clean: # shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	# . venv/bin/activate; python setup.py develop

launch: venv # shutdown
	. venv/bin/activate; python coronaRes.py 

shutdown:
	ps -ef | grep "server.py" | grep -v grep | awk '{print $$2}' | xargs kill
