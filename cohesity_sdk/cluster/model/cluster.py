"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cluster.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    AuditLogConfig
    ClusterAuditLogConfig
    ClusterCreateNetworkConfig
    ClusterProxyServerConfig
    RigelClusterConfigParams
    ViewsGlobalSettings


class Cluster(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {
        ('cluster_size',): {
            'None': None,
            'SMALL': "Small",
            'MEDIUM': "Medium",
            'LARGE': "Large",
            'XLARGE': "XLarge",
            'NEXTGEN': "NextGen",
        },
        ('type',): {
            'None': None,
            'PHYSICAL': "Physical",
            'VIRTUAL': "Virtual",
            'CLOUD': "Cloud",
            'RIGEL': "Rigel",
            'UNKNOWN': "Unknown",
            'HELIOSONPREMVM': "HeliosOnPremVM",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'cluster_audit_log_config': (ClusterAuditLogConfig,),  # noqa: E501
            'cluster_size': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'enable_encryption': (bool,),  # noqa: E501
            'file_services_audit_log_config': (AuditLogConfig,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'incarnation_id': (int,),  # noqa: E501
            'local_tenant_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'network_config': (ClusterCreateNetworkConfig,),  # noqa: E501
            'proxy_server_config': (ClusterProxyServerConfig,),  # noqa: E501
            'region_id': (str,),  # noqa: E501
            'rigel_cluster_params': (RigelClusterConfigParams,),  # noqa: E501
            'sw_version': (str,),  # noqa: E501
            'tenant_id': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'views_global_settings': (ViewsGlobalSettings,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'cluster_audit_log_config': 'clusterAuditLogConfig',  # noqa: E501
        'cluster_size': 'clusterSize',  # noqa: E501
        'description': 'description',  # noqa: E501
        'enable_encryption': 'enableEncryption',  # noqa: E501
        'file_services_audit_log_config': 'fileServicesAuditLogConfig',  # noqa: E501
        'id': 'id',  # noqa: E501
        'incarnation_id': 'incarnationId',  # noqa: E501
        'local_tenant_id': 'localTenantId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'network_config': 'networkConfig',  # noqa: E501
        'proxy_server_config': 'proxyServerConfig',  # noqa: E501
        'region_id': 'regionId',  # noqa: E501
        'rigel_cluster_params': 'rigelClusterParams',  # noqa: E501
        'sw_version': 'swVersion',  # noqa: E501
        'tenant_id': 'tenantId',  # noqa: E501
        'type': 'type',  # noqa: E501
        'views_global_settings': 'viewsGlobalSettings',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Cluster - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)

            cluster_audit_log_config (ClusterAuditLogConfig): [optional]  # noqa: E501
            cluster_size (str): Specifies the size of the cloud platforms.. [optional]  # noqa: E501
            description (str): Description of the cluster.. [optional]  # noqa: E501
            enable_encryption (bool): Specifies whether or not encryption is enabled. If encryption is enabled, all data on the Cluster will be encrypted.. [optional]  # noqa: E501
            file_services_audit_log_config (AuditLogConfig): [optional]  # noqa: E501
            id (int): Specifies the cluster id of the new cluster.. [optional]  # noqa: E501
            incarnation_id (int): Specifies the incarnation id of the new cluster.. [optional]  # noqa: E501
            local_tenant_id (str): Specifies the local tenant id. Only applicable on Helios.. [optional]  # noqa: E501
            name (str): Name of the new cluster.. [optional]  # noqa: E501
            network_config (ClusterCreateNetworkConfig): [optional]  # noqa: E501
            proxy_server_config (ClusterProxyServerConfig): [optional]  # noqa: E501
            region_id (str): Specifies the region id on which this cluster is present. Only applicable on Helios for DMaaS clusters.. [optional]  # noqa: E501
            rigel_cluster_params (RigelClusterConfigParams): [optional]  # noqa: E501
            sw_version (str): Software version of the new cluster.. [optional]  # noqa: E501
            tenant_id (str): Specifies the globally unique tenant id. Only applicable on Helios.. [optional]  # noqa: E501
            type (str): Specifies the type of the new cluster.. [optional]  # noqa: E501
            views_global_settings (ViewsGlobalSettings): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)


        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


