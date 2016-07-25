===========================
Hello World Spring REST API
===========================

This is a minimal web application to expose a single OAuth-secured ``/hello`` endpoint.

How to build and run:

.. code-block:: bash

    $ sudo pip3 install -U scm-source
    $ ./mvnw clean package
    $ scm-source -f target/scm-source.json
    $ docker build -t helloworld .
    $ docker run -it -p 8080:8080 -e TOKENINFO_URL=https://info.services.auth.zalando.com/oauth2/tokeninfo helloworld

Testing the OAuth secured endpoint:

.. code-block:: bash

    $ sudo pip3 install -U httpie-zign
    $ echo '{"default_options": ["--auth-type=zign"]}' > ~/.httpie/config.json
    $ http -a test: http://localhost:8080/hello
