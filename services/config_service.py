import os

print('Load environments')

def __get_env_value(env_key, default_key=None):
    return os.getenv(env_key, default_key)

def get_selenium_url():
    return __get_env_value('SELENIUM_URL', 'http://selenium-hub:4444')

def get_action_links():
    return ['https://www.thalgo-usa.com/face/_/psa/956-face/20-action/101-cleanser---foaming/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/102-waters-&-lotions/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/88-masks-&-scrubs/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/86-serum-&-concentrate/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/89-eye-contour/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/139-day-care/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/106-night-care/',
            'https://www.thalgo-usa.com/face/_/psa/956-face/20-action/188-lip-balm/']
