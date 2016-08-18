===========================
Hello World Spring REST API
===========================

This is a minimal web application to expose a single OAuth-secured ``/hello`` endpoint.

How to build and run:

.. code-block:: bash

    $ ./mvnw clean package
    $ export TOKENINFO_URL=https://info.services.auth.zalando.com/oauth2/tokeninfo
    $ java -jar target/helloworld-1.0.0-SNAPSHOT.jar

Testing the OAuth secured endpoint:

.. code-block:: bash

    $ sudo pip3 install -U httpie-zign
    $ echo '{"default_options": ["--auth-type=zign"]}' > ~/.httpie/config.json
    $ zign token
    $ http -a test: http://localhost:8080/hello
