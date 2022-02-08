from cohesity_sdk.cohesity_client_v2.configuration import Configuration
from cohesity_sdk.cohesity_client_v2.api_client import ApiClient
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
#from cohesity_sdk.cohesity_client_v2.model.create_access_token_request_params import CreateAccessTokenRequestParams


from cohesity_sdk.cohesity_client_v2.api.active_directory import ActiveDirectoryApi
from cohesity_sdk.cohesity_client_v2.api.audit_log import AuditLogApi
from cohesity_sdk.cohesity_client_v2.api.connectors import ConnectorsApi
from cohesity_sdk.cohesity_client_v2.api.d_maa_s_tenant_certificate import DMaaSTenantCertificateApi
from cohesity_sdk.cohesity_client_v2.api.data_tiering import DataTieringApi
from cohesity_sdk.cohesity_client_v2.api.external_connection import ExternalConnectionApi
from cohesity_sdk.cohesity_client_v2.api.failover import FailoverApi
from cohesity_sdk.cohesity_client_v2.api.fleet_instance import FleetInstanceApi
from cohesity_sdk.cohesity_client_v2.api.helios_registration import HeliosRegistrationApi
from cohesity_sdk.cohesity_client_v2.api.internal import InternalApi
from cohesity_sdk.cohesity_client_v2.api.kerberos_providers import KerberosProvidersApi
from cohesity_sdk.cohesity_client_v2.api.keystone import KeystoneApi
from cohesity_sdk.cohesity_client_v2.api.mfa import MfaApi
from cohesity_sdk.cohesity_client_v2.api.miscellaneous import MiscellaneousApi
from cohesity_sdk.cohesity_client_v2.api.network_information_service__nis import NetworkInformationServiceNISApi
from cohesity_sdk.cohesity_client_v2.api.node_groups import NodeGroupsApi
from cohesity_sdk.cohesity_client_v2.api.objects import ObjectsApi
from cohesity_sdk.cohesity_client_v2.api.patches import PatchesApi
from cohesity_sdk.cohesity_client_v2.api.platform import PlatformApi
from cohesity_sdk.cohesity_client_v2.api.protected_objects import ProtectedObjectsApi
from cohesity_sdk.cohesity_client_v2.api.protection_groups import ProtectionGroupsApi
from cohesity_sdk.cohesity_client_v2.api.protection_policies import ProtectionPoliciesApi
from cohesity_sdk.cohesity_client_v2.api.protection_sources import ProtectionSourcesApi
from cohesity_sdk.cohesity_client_v2.api.recoveries import RecoveriesApi
from cohesity_sdk.cohesity_client_v2.api.remote_clusters import RemoteClustersApi
from cohesity_sdk.cohesity_client_v2.api.search import SearchApi
from cohesity_sdk.cohesity_client_v2.api.security import SecurityApi
from cohesity_sdk.cohesity_client_v2.api.stats import StatsApi
from cohesity_sdk.cohesity_client_v2.api.storage_domains import StorageDomainsApi
from cohesity_sdk.cohesity_client_v2.api.tags import TagsApi
from cohesity_sdk.cohesity_client_v2.api.tasks import TasksApi
from cohesity_sdk.cohesity_client_v2.api.tenants import TenantsApi
from cohesity_sdk.cohesity_client_v2.api.test_data_management import TestDataManagementApi
from cohesity_sdk.cohesity_client_v2.api.users import UsersApi
from cohesity_sdk.cohesity_client_v2.api.views import ViewsApi
from cohesity_sdk.cohesity_client_v2.api.network_reset import NetworkResetApi

import re
from urllib3.exceptions import MaxRetryError

class lazy_property(object):

    """A decorator class for lazy instantiation."""

    def __init__(self, fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj, self.func_name, value)
        return value


# class Cohesity_client_v2Client:
class CohesityClientV2:
    def __init__(self,
        cluster_vip = None,
        username = None,
        password = None,
        domain = None,
        api_key = None,
        auth_timeout = 30
    ):

        self.domain = domain
        self.username = username
        self.password = password
        self.api_key = api_key
        self.auth_timeout = auth_timeout

        self.configuration = Configuration()
        if cluster_vip != None:
            host = re.sub("localhost", cluster_vip, self.configuration._base_path)
            host = re.sub("http:", "https:", host)
            self.configuration.host = host
        else:
            raise Exception('Missing cluster_vip info to initialize a client.')
            # for potential use case
            # self.configuration.host = 'https://xxx.cohesity.com/v2'

        # TODO: remove this later, python in MacOS Catalina has a problem in verify SSL
        self.configuration.verify_ssl = False

        # This fixes the response type conflict between the backend and Swagger spec file
        self.configuration.discard_unknown_keys = True

        if username == None and password == None and api_key == None:
            raise Exception('Missing authentication info to initialize a client. \
                Please provide authentication info.')

        self.__authenticate()

    def __get_token(self):
        # TODO: change the hard-coded host

        with ApiClient(self.configuration) as api_client:
            api_instance = AccessTokensApi(api_client)
            body = CreateAccessTokenRequestParams(
                domain=self.domain,
                password=self.password,
                username=self.username
            )

            try:
                return api_instance.create_access_token(body, _request_timeout=self.auth_timeout)
            except MaxRetryError as e:
                raise ApiException(status=404, reason=str(e)) from None

    def __authenticate(self):
        if self.username and self.password and self.domain:
            token = self.__get_token()
            self.configuration.api_key['TokenHeader'] = token.token_type + ' ' + token.access_token
        elif self.api_key:
            self.configuration.api_key['APIKeyHeader'] = self.api_key



    @lazy_property
    def active_directory(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ActiveDirectoryApi(api_client)

    @lazy_property
    def audit_log(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AuditLogApi(api_client)

    @lazy_property
    def connectors(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ConnectorsApi(api_client)

    @lazy_property
    def d_maa_s_tenant_certificate(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return DMaaSTenantCertificateApi(api_client)

    @lazy_property
    def data_tiering(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return DataTieringApi(api_client)

    @lazy_property
    def external_connection(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ExternalConnectionApi(api_client)

    @lazy_property
    def failover(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FailoverApi(api_client)

    @lazy_property
    def fleet_instance(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FleetInstanceApi(api_client)

    @lazy_property
    def helios_registration(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosRegistrationApi(api_client)

    @lazy_property
    def internal(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return InternalApi(api_client)

    @lazy_property
    def kerberos_providers(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KerberosProvidersApi(api_client)

    @lazy_property
    def keystone(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeystoneApi(api_client)

    @lazy_property
    def mfa(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MfaApi(api_client)

    @lazy_property
    def miscellaneous(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MiscellaneousApi(api_client)

    @lazy_property
    def network_information_service__nis(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkInformationServiceNISApi(api_client)

    @lazy_property
    def node_groups(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NodeGroupsApi(api_client)

    @lazy_property
    def objects(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ObjectsApi(api_client)

    @lazy_property
    def patches(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PatchesApi(api_client)

    @lazy_property
    def platform(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PlatformApi(api_client)

    @lazy_property
    def protected_objects(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectedObjectsApi(api_client)

    @lazy_property
    def protection_groups(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionGroupsApi(api_client)

    @lazy_property
    def protection_policies(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionPoliciesApi(api_client)

    @lazy_property
    def protection_sources(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionSourcesApi(api_client)

    @lazy_property
    def recoveries(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RecoveriesApi(api_client)

    @lazy_property
    def remote_clusters(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteClustersApi(api_client)

    @lazy_property
    def search(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SearchApi(api_client)

    @lazy_property
    def security(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SecurityApi(api_client)

    @lazy_property
    def stats(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StatsApi(api_client)

    @lazy_property
    def storage_domains(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StorageDomainsApi(api_client)

    @lazy_property
    def tags(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TagsApi(api_client)

    @lazy_property
    def tasks(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TasksApi(api_client)

    @lazy_property
    def tenants(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TenantsApi(api_client)

    @lazy_property
    def test_data_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TestDataManagementApi(api_client)

    @lazy_property
    def users(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UsersApi(api_client)

    @lazy_property
    def views(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ViewsApi(api_client)

    @lazy_property
    def network_reset(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkResetApi(api_client)
