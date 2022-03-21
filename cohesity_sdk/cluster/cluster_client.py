from cohesity_sdk.cluster.configuration import Configuration
from cohesity_sdk.cluster.api_client import ApiClient
from cohesity_sdk.cluster.exceptions import ApiException
from cohesity_sdk.cluster.model.create_access_token_request_params import CreateAccessTokenRequestParams


from cohesity_sdk.cluster.api.access_token import AccessTokenApi
from cohesity_sdk.cluster.api.active_directory import ActiveDirectoryApi
from cohesity_sdk.cluster.api.agent import AgentApi
from cohesity_sdk.cluster.api.alert import AlertApi
from cohesity_sdk.cluster.api.antivirus_service import AntivirusServiceApi
from cohesity_sdk.cluster.api.audit_log import AuditLogApi
from cohesity_sdk.cluster.api.cloud_retrieve_task import CloudRetrieveTaskApi
from cohesity_sdk.cluster.api.connectors import ConnectorsApi
from cohesity_sdk.cluster.api.d_maa_s_tenant_certificate import DMaaSTenantCertificateApi
from cohesity_sdk.cluster.api.data_tiering import DataTieringApi
from cohesity_sdk.cluster.api.external_connection import ExternalConnectionApi
from cohesity_sdk.cluster.api.external_target import ExternalTargetApi
from cohesity_sdk.cluster.api.failover import FailoverApi
from cohesity_sdk.cluster.api.firewall import FirewallApi
from cohesity_sdk.cluster.api.fleet_instance import FleetInstanceApi
from cohesity_sdk.cluster.api.helios_on_prem import HeliosOnPremApi
from cohesity_sdk.cluster.api.ips import IPsApi
from cohesity_sdk.cluster.api.identity_provider import IdentityProviderApi
from cohesity_sdk.cluster.api.indexing_cloud_config import IndexingCloudConfigApi
from cohesity_sdk.cluster.api.internal import InternalApi
from cohesity_sdk.cluster.api.kerberos_provider import KerberosProviderApi
from cohesity_sdk.cluster.api.key_management_system import KeyManagementSystemApi
from cohesity_sdk.cluster.api.keystone import KeystoneApi
from cohesity_sdk.cluster.api.ldap import LDAPApi
from cohesity_sdk.cluster.api.mfa import MFAApi
from cohesity_sdk.cluster.api.marketplace_app import MarketplaceAppApi
from cohesity_sdk.cluster.api.network_information_service import NetworkInformationServiceApi
from cohesity_sdk.cluster.api.node_group import NodeGroupApi
from cohesity_sdk.cluster.api.object import ObjectApi
from cohesity_sdk.cluster.api.patch_management import PatchManagementApi
from cohesity_sdk.cluster.api.platform import PlatformApi
from cohesity_sdk.cluster.api.policy import PolicyApi
from cohesity_sdk.cluster.api.privilege import PrivilegeApi
from cohesity_sdk.cluster.api.protected_object import ProtectedObjectApi
from cohesity_sdk.cluster.api.protection_group import ProtectionGroupApi
from cohesity_sdk.cluster.api.recovery import RecoveryApi
from cohesity_sdk.cluster.api.registration import RegistrationApi
from cohesity_sdk.cluster.api.remote_clusters import RemoteClustersApi
from cohesity_sdk.cluster.api.remote_storage import RemoteStorageApi
from cohesity_sdk.cluster.api.role import RoleApi
from cohesity_sdk.cluster.api.routes import RoutesApi
from cohesity_sdk.cluster.api.search import SearchApi
from cohesity_sdk.cluster.api.security import SecurityApi
from cohesity_sdk.cluster.api.source import SourceApi
from cohesity_sdk.cluster.api.stats import StatsApi
from cohesity_sdk.cluster.api.storage_domain import StorageDomainApi
from cohesity_sdk.cluster.api.syslog import SyslogApi
from cohesity_sdk.cluster.api.tag import TagApi
from cohesity_sdk.cluster.api.tasks import TasksApi
from cohesity_sdk.cluster.api.tenant import TenantApi
from cohesity_sdk.cluster.api.test_data_management import TestDataManagementApi
from cohesity_sdk.cluster.api.uda_connector_config import UdaConnectorConfigApi
from cohesity_sdk.cluster.api.user import UserApi
from cohesity_sdk.cluster.api.view import ViewApi
from cohesity_sdk.cluster.api.network_reset import NetworkResetApi
from cohesity_sdk.cluster.api.runbooks import RunbooksApi

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


class ClusterClient:
#class CohesityClient:
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
            api_instance = AccessTokenApi(api_client)
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
    def access_token(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AccessTokenApi(api_client)

    @lazy_property
    def active_directory(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ActiveDirectoryApi(api_client)

    @lazy_property
    def agent(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AgentApi(api_client)

    @lazy_property
    def alert(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AlertApi(api_client)

    @lazy_property
    def antivirus_service(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AntivirusServiceApi(api_client)

    @lazy_property
    def audit_log(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return AuditLogApi(api_client)

    @lazy_property
    def cloud_retrieve_task(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return CloudRetrieveTaskApi(api_client)

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
    def external_target(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ExternalTargetApi(api_client)

    @lazy_property
    def failover(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FailoverApi(api_client)

    @lazy_property
    def firewall(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FirewallApi(api_client)

    @lazy_property
    def fleet_instance(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return FleetInstanceApi(api_client)

    @lazy_property
    def helios_on_prem(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return HeliosOnPremApi(api_client)

    @lazy_property
    def ips(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IPsApi(api_client)

    @lazy_property
    def identity_provider(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IdentityProviderApi(api_client)

    @lazy_property
    def indexing_cloud_config(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return IndexingCloudConfigApi(api_client)

    @lazy_property
    def internal(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return InternalApi(api_client)

    @lazy_property
    def kerberos_provider(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KerberosProviderApi(api_client)

    @lazy_property
    def key_management_system(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeyManagementSystemApi(api_client)

    @lazy_property
    def keystone(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return KeystoneApi(api_client)

    @lazy_property
    def ldap(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return LDAPApi(api_client)

    @lazy_property
    def mfa(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MFAApi(api_client)

    @lazy_property
    def marketplace_app(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return MarketplaceAppApi(api_client)

    @lazy_property
    def network_information_service(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkInformationServiceApi(api_client)

    @lazy_property
    def node_group(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NodeGroupApi(api_client)

    @lazy_property
    def object(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ObjectApi(api_client)

    @lazy_property
    def patch_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PatchManagementApi(api_client)

    @lazy_property
    def platform(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PlatformApi(api_client)

    @lazy_property
    def policy(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PolicyApi(api_client)

    @lazy_property
    def privilege(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return PrivilegeApi(api_client)

    @lazy_property
    def protected_object(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectedObjectApi(api_client)

    @lazy_property
    def protection_group(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ProtectionGroupApi(api_client)

    @lazy_property
    def recovery(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RecoveryApi(api_client)

    @lazy_property
    def registration(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RegistrationApi(api_client)

    @lazy_property
    def remote_clusters(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteClustersApi(api_client)

    @lazy_property
    def remote_storage(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RemoteStorageApi(api_client)

    @lazy_property
    def role(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoleApi(api_client)

    @lazy_property
    def routes(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RoutesApi(api_client)

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
    def source(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SourceApi(api_client)

    @lazy_property
    def stats(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StatsApi(api_client)

    @lazy_property
    def storage_domain(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return StorageDomainApi(api_client)

    @lazy_property
    def syslog(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return SyslogApi(api_client)

    @lazy_property
    def tag(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TagApi(api_client)

    @lazy_property
    def tasks(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TasksApi(api_client)

    @lazy_property
    def tenant(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TenantApi(api_client)

    @lazy_property
    def test_data_management(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return TestDataManagementApi(api_client)

    @lazy_property
    def uda_connector_config(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UdaConnectorConfigApi(api_client)

    @lazy_property
    def user(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return UserApi(api_client)

    @lazy_property
    def view(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return ViewApi(api_client)

    @lazy_property
    def network_reset(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return NetworkResetApi(api_client)

    @lazy_property
    def runbooks(self):
        self.__authenticate()
        with ApiClient(self.configuration) as api_client:
            return RunbooksApi(api_client)
