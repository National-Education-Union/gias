from requests import get, post, exceptions
from datetime import datetime


class GiasApi:
    __base_url__ = (
        'https://api-customerengagement.platform.education.gov.uk/gias/'
        )
    __user_agent__ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    __get_timeout__ = 10
    __get_gias_multiple_results_limit__ = 1000


    def __init__(
            self,
            client_id,
            primary_secret,
            scope,
            api_key,
            token_endpoint
            ):
        self.__client_id__ = client_id
        self.__primary_secret__ = primary_secret
        self.__scope__ = scope
        self.__api_key__ = api_key
        self.__token_endpoint__ = token_endpoint
        self.__get_access_token__()
        

    def __get_access_token__(self):
        call_time = datetime.now()
        try:
            response = post(
                self.__token_endpoint__,
                headers={'content-type': 'application/x-www-form-urlencoded'},
                data={
                    'grant_type': 'client_credentials',
                    'client_id': self.__client_id__,
                    'client_secret': self.__primary_secret__,
                    'scope': self.__scope__,
                    }
                )
        except Exception as e:
            raise Exception('Access token request failed.', e)
        if response.ok:
            self.__token_created__ = call_time
            self.__headers__ = {
                'Authorization': 'Bearer ' + response.json()['access_token'],
                'Ocp-Apim-Subscription-Key': self.__api_key__,
                'user-agent': self.__user_agent__
                }
        else:
            raise Exception(f'Access token request failed.\n{response.text}')


    def __check_access_token__(self):
        if (datetime.now() - self.__token_created__).seconds > 3500:
            self.__get_access_token__()


    def __get_gias__(self, request):
        self.__check_access_token__()
        timeout_error = True
        while timeout_error:
            try:
                response = get(
                    f'{self.__base_url__}{request}',
                    headers=self.__headers__,
                    timeout=self.__get_timeout__
                    )
                timeout_error = False
            except exceptions.Timeout:
                print('Connection timed out. Trying again...')
                timeout_error = True
        if response.ok:
            return response.json()
        else:
            raise Exception(response.text)


    def establishment(self, urn):
        return self.__get_gias__(f'establishment/{urn}')


    def establishment_changes(self, urn):
        return self.__get_gias__(f'establishment/{urn}/changes')


    def establishment_groups(self, urn):
        return self.__get_gias__(f'establishment/{urn}/groups')


    def establishment_governors(self, urn):
        return self.__get_gias__(f'establishment/{urn}/governors')


    def establishment_sentypes(self, urn):
        return self.__get_gias__(f'establishment/{urn}/sentypes')


    def group(self, uid):
        return self.__get_gias__(f'group/{uid}')


    def group_establishments(self, uid):
        return self.__get_gias__(f'group/{uid}/establishments')


    def group_changes(self, uid):
        return self.__get_gias__(f'group/{uid}/changes')


    def governor(self, gid):
        return self.__get_gias__(f'governor/{gid}')


    def governor_establishments(self, gid):
        return self.__get_gias__(f'governor/{gid}/establishments')


    def governor_changes(self, gid):
        return self.__get_gias__(f'governor/{gid}/changes')


    def __get_gias_all__(self, data_group):
        limit = self.__get_gias_multiple_results_limit__
        offset = 0
        data = []
        next_data = None
        while next_data != []:
            next_data = self.__get_gias__(
                f'{data_group}/all?limit={limit}&offset={offset}'
                )
            if type(next_data) == list:
                data.extend(next_data)
                offset += limit
            print(f'Records found: {len(data)}')
        return data


    def establishments(self):
        return self.__get_gias_all__('establishment')


    def groups(self):
        return self.__get_gias_all__('group')


    def governors(self):
        return self.__get_gias_all__('governor')


    def search(self, query, timeout=10):
        self.__check_access_token__()
        timeout_error = True
        while timeout_error:
            try:
                response = post(
                    f'{self.__base_url__}search',
                    headers=self.__headers__,
                    data=query,
                    timeout=timeout,
                    )
                timeout_error = False
            except exceptions.Timeout:
                print('Connection timed out. Trying again...')
                timeout_error = True
        if response.ok:
            return response.json()
        else:
            raise Exception(response.text)
