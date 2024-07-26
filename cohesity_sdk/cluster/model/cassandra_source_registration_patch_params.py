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
    from cohesity_sdk.cluster.model.cassandra_source_registration_patch_params_cassandra_credentials import CassandraSourceRegistrationPatchParamsCassandraCredentials
    from cohesity_sdk.cluster.model.cassandra_source_registration_patch_params_jmx_credentials import CassandraSourceRegistrationPatchParamsJmxCredentials
    from cohesity_sdk.cluster.model.dse_solr_info import DSESolrInfo
    from cohesity_sdk.cluster.model.ssh_password_credentials import SshPasswordCredentials
    from cohesity_sdk.cluster.model.ssh_private_key_credentials import SshPrivateKeyCredentials
    globals()['CassandraSourceRegistrationPatchParamsCassandraCredentials'] = CassandraSourceRegistrationPatchParamsCassandraCredentials
    globals()['CassandraSourceRegistrationPatchParamsJmxCredentials'] = CassandraSourceRegistrationPatchParamsJmxCredentials
    globals()['DSESolrInfo'] = DSESolrInfo
    globals()['SshPasswordCredentials'] = SshPasswordCredentials
    globals()['SshPrivateKeyCredentials'] = SshPrivateKeyCredentials


class CassandraSourceRegistrationPatchParams(ModelNormal):
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
            'cassandra_credentials': (CassandraSourceRegistrationPatchParamsCassandraCredentials,),  # noqa: E501
            'commit_log_backup_location': (str, none_type,),  # noqa: E501
            'config_directory': (str, none_type,),  # noqa: E501
            'data_center_names': ([str],),  # noqa: E501
            'dse_configuration_directory': (str, none_type,),  # noqa: E501
            'dse_solr_info': (DSESolrInfo,),  # noqa: E501
            'is_dse_authenticator': (bool, none_type,),  # noqa: E501
            'is_dse_tiered_storage': (bool, none_type,),  # noqa: E501
            'jmx_credentials': (CassandraSourceRegistrationPatchParamsJmxCredentials,),  # noqa: E501
            'kerberos_principal': (str, none_type,),  # noqa: E501
            'seed_node': (str, none_type,),  # noqa: E501
            'ssh_password_credentials': (SshPasswordCredentials,),  # noqa: E501
            'ssh_private_key_credentials': (SshPrivateKeyCredentials,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'cassandra_credentials': 'cassandraCredentials',  # noqa: E501
        'commit_log_backup_location': 'commitLogBackupLocation',  # noqa: E501
        'config_directory': 'configDirectory',  # noqa: E501
        'data_center_names': 'dataCenterNames',  # noqa: E501
        'dse_configuration_directory': 'dseConfigurationDirectory',  # noqa: E501
        'dse_solr_info': 'dseSolrInfo',  # noqa: E501
        'is_dse_authenticator': 'isDseAuthenticator',  # noqa: E501
        'is_dse_tiered_storage': 'isDseTieredStorage',  # noqa: E501
        'jmx_credentials': 'jmxCredentials',  # noqa: E501
        'kerberos_principal': 'kerberosPrincipal',  # noqa: E501
        'seed_node': 'seedNode',  # noqa: E501
        'ssh_password_credentials': 'sshPasswordCredentials',  # noqa: E501
        'ssh_private_key_credentials': 'sshPrivateKeyCredentials',  # noqa: E501
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
        """CassandraSourceRegistrationPatchParams - a model defined in OpenAPI

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

            cassandra_credentials (CassandraSourceRegistrationPatchParamsCassandraCredentials): [optional]  # noqa: E501
            commit_log_backup_location (str, none_type): Commit Logs backup location on cassandra nodes. [optional]  # noqa: E501
            config_directory (str, none_type): Directory path containing Cassandra configuration YAML file.. [optional]  # noqa: E501
            data_center_names ([str]): Data centers for this cluster.. [optional]  # noqa: E501
            dse_configuration_directory (str, none_type): Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra.. [optional]  # noqa: E501
            dse_solr_info (DSESolrInfo): [optional]  # noqa: E501
            is_dse_authenticator (bool, none_type): Set to true if this cluster has DSE Authenticator.. [optional]  # noqa: E501
            is_dse_tiered_storage (bool, none_type): Set to true if this cluster has DSE tiered storage.. [optional]  # noqa: E501
            jmx_credentials (CassandraSourceRegistrationPatchParamsJmxCredentials): [optional]  # noqa: E501
            kerberos_principal (str, none_type): Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.). [optional]  # noqa: E501
            seed_node (str, none_type): Any one seed node of the Cassandra cluster.. [optional]  # noqa: E501
            ssh_password_credentials (SshPasswordCredentials): [optional]  # noqa: E501
            ssh_private_key_credentials (SshPrivateKeyCredentials): [optional]  # noqa: E501
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


