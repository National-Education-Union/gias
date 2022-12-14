from requests import get, post, exceptions
from datetime import datetime


class GetInformationAboutSchools:
    __base_url__ = (
        'https://api-customerengagement.platform.education.gov.uk/gias/'
        )
    __user_agent__ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    __timeout_get__ = 10
    __limit_multiple_results__ = 5


    def __init__(
            self,
            client_id,
            primary_secret,
            scope,
            api_key,
            token_endpoint
            ):
        """
        Wrapper for DfE's Get Information About Schools API.

        Parameters
        ----------
        client_id : str
            Your GIAS app's Client ID.
        primary_secret : str
            Your GIAS app's primary secret.
        scope : str
            The URL of your app's scope.
        api_key : str
            Your GIAS app's API key.
        token_endpoint : str
            The URL of the token endpoint for your GIAS app.

        Returns
        -------
        None.

        """
        self.__client_id__ = client_id
        self.__primary_secret__ = primary_secret
        self.__scope__ = scope
        self.__api_key__ = api_key
        self.__token_endpoint__ = token_endpoint
        self.__get_access_token__()

    def __get_access_token__(self):
        """
        Requsts access token from GIAS API.

        Raises
        ------
        Exception
            If access token request fails.

        Returns
        -------
        None.

        """

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
        """
        Checks if access token is still valid and fetches a new one if not.

        Returns
        -------
        None.

        """
        if (datetime.now() - self.__token_created__).seconds > 3500:
            self.__get_access_token__()


    def __get__(self, request):
        """
        Makes GET request to GIAS API.

        Parameters
        ----------
        request : str
            Request string.

        Raises
        ------
        Exception
            If request fails.

        Returns
        -------
        dict
            Response to request.

        """
        self.__check_access_token__()
        timeout_error = True
        while timeout_error:
            try:
                response = get(
                    f'{self.__base_url__}{request}',
                    headers=self.__headers__,
                    timeout=self.__timeout_get__
                    )
                timeout_error = False
            except exceptions.Timeout:
                print(
                    f"\r{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - \
Connection timed out. Trying again...",
                    end=""
                    )
                timeout_error = True
        if response.ok:
            return response.json()
        else:
            raise Exception(response.text)


    def establishment(self, urn):
        """
        Gets GIAS establishment details.

        Parameters
        ----------
        urn : int, str
            URN of establishment.

        Returns
        -------
        dict
            Establishment's details.

        """

        return self.__get__(f'establishment/{urn}')


    def establishment_changes(self, urn):
        """
        Gets GIAS establishment changes.

        Parameters
        ----------
        urn : int, str
            URN of establishment.

        Returns
        -------
        list
            Establishment's changes - each change is a dict.

        """
        return self.__get__(f'establishment/{urn}/changes')


    def establishment_groups(self, urn):
        """
        Gets GIAS establishment groups.

        Parameters
        ----------
        urn : int, str
            URN of establishment.

        Returns
        -------
        list
            Establishment's groups' UIDs - each group is a dict.

        """
        return self.__get__(f'establishment/{urn}/groups')


    def establishment_governors(self, urn):
        """
        Gets GIAS establishment governors.

        Parameters
        ----------
        urn : int, str
            URN of establishment.

        Returns
        -------
        list
            Establishment's governors' GIDs - each governor is a dict.

        """
        return self.__get__(f'establishment/{urn}/governors')


    def establishment_sentypes(self, urn):
        """
        Gets GIAS establishment SEN types.

        Parameters
        ----------
        urn : int, str
            URN of establishment.

        Returns
        -------
        list
            Establishment's SEN types - each SEN type is a dict.

        """
        return self.__get__(f'establishment/{urn}/sentypes')


    def group(self, uid):
        """
        Gets GIAS group details.

        Parameters
        ----------
        urn : int, str
            UID of group.

        Returns
        -------
        dict
            Group details.

        """
        return self.__get__(f'group/{uid}')


    def group_establishments(self, uid):
        """
        Gets GIAS group establishments.

        Parameters
        ----------
        urn : int, str
            UID of group.

        Returns
        -------
        list
            Group's establishments' URNs - each URN is a dict.

        """
        return self.__get__(f'group/{uid}/establishments')


    def group_changes(self, uid):
        """
        Gets GIAS group changes.

        Parameters
        ----------
        urn : int, str
            UID of group.

        Returns
        -------
        list
            Group's changes - each change is a dict.

        """
        return self.__get__(f'group/{uid}/changes')


    def governor(self, gid):
        """
        Gets GIAS governor details.

        Parameters
        ----------
        urn : int, str
            Governor GID.

        Returns
        -------
        dict
            Governor's details.

        """
        return self.__get__(f'governor/{gid}')


    def governor_establishments(self, gid):
        """
        Gets GIAS governor establishments.

        Parameters
        ----------
        urn : int, str
            Governor GID.

        Returns
        -------
        list
            Governor's establishments' URNs - each URN is a dict.

        """
        return self.__get__(f'governor/{gid}/establishments')


    def governor_changes(self, gid):
        """
        Gets GIAS governor changes.

        Parameters
        ----------
        urn : int, str
            Governor GID.

        Returns
        -------
        list
            Governor's changes - each change is a dict.

        """
        return self.__get__(f'governor/{gid}/changes')


    def __get_all__(self, data_group):
        """
        Gets details of all establishments, groups or governors.

        Parameters
        ----------
        data_group : str
            'establishment', 'group' or 'governor' 

        Returns
        -------
        data : list
            All establishments', groups' or governors' details - each set of details is a dict.

        """
        limit = self.__limit_multiple_results__
        offset = 0
        data = []
        next_data = None
        print(
            f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - \
Started getting all {data_group}s"
            )
        while next_data != []:
            try:
                next_data = self.__get__(
                    f'{data_group}?limit={limit}&offset={offset}'
                    )
                if type(next_data) == list:
                    data.extend(next_data)
                    offset += limit
                print(
                    f"\r{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - \
Records found: {len(data)}                   ",
                    end=""
                    )
            except Exception as e:
                print(f'{str(e)}\nOffset: {offset}')
        return data


    def establishments(self):
        """
        Gets all GIAS establishments' details.

        Returns
        -------
        list
            All establishments - each establishment is a dict.

        """

        return self.__get_all__('establishment')


    def groups(self):
        """
        Gets all GIAS groups' details.

        Returns
        -------
        list
            All groups - each group is a dict.

        """
        return self.__get_all__('group')


    def governors(self):
        """
        Gets all GIAS governors' details.

        Returns
        -------
        list
            All governors - each governor is a dict.

        """
        return self.__get_all__('governor')


    def search(self, query, timeout=30):
        """
        Posts a GraphQL search to the GIAS API.

        Parameters
        ----------
        query : str
            A GraphQL query written as a string.
        timeout : int, optional
            Timeout for request. The default is 10.

        Raises
        ------
        Exception
            If request fails.

        Returns
        -------
        dict
            Result of GraphQL query.

        """
        self.__check_access_token__()
        timeout_error = True
        while timeout_error:
            try:
                response = post(
                    f'{self.__base_url__}search',
                    headers=self.__headers__,
                    json={'query': query},
                    timeout=timeout,
                    )
                timeout_error = False
            except exceptions.Timeout:
                print(
                    f"\r{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - \
Connection timed out. Trying again...",
                    end=""
                    )
                timeout_error = True
        if response.ok:
            return response.json()
        else:
            raise Exception(response.text)
