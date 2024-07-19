ifneq (,$(wildcard ./.env))
   include .env
   export
   ENV_FILE_PARAM = --env-file .env
endif

secret-key:
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

secret-base64:
	@export SECRET_KEY=$$(python -c "from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())") && \
	echo "Secret key is: $$SECRET_KEY" && \
	export SECRET_KEY_ENCODED=$$(echo "$$SECRET_KEY" | base64) && \
	echo "Base64 Encoded Secret key is: $$SECRET_KEY_ENCODED"