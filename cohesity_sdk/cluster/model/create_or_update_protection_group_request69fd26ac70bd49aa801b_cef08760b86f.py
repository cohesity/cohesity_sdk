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
    from cohesity_sdk.cluster.model.acropolis_protection_group_params import AcropolisProtectionGroupParams
    from cohesity_sdk.cluster.model.ad_protection_group_params import ADProtectionGroupParams
    from cohesity_sdk.cluster.model.aws_protection_group_params import AwsProtectionGroupParams
    from cohesity_sdk.cluster.model.azure_protection_group_params import AzureProtectionGroupParams
    from cohesity_sdk.cluster.model.cassandra_protection_group_params import CassandraProtectionGroupParams
    from cohesity_sdk.cluster.model.create_or_update_protection_group_request_all_of import CreateOrUpdateProtectionGroupRequestAllOf
    from cohesity_sdk.cluster.model.elastifile_protection_group_params import ElastifileProtectionGroupParams
    from cohesity_sdk.cluster.model.exchange_protection_group_params import ExchangeProtectionGroupParams
    from cohesity_sdk.cluster.model.flashblade_protection_group_params import FlashbladeProtectionGroupParams
    from cohesity_sdk.cluster.model.gcp_protection_group_params import GcpProtectionGroupParams
    from cohesity_sdk.cluster.model.generic_nas_protection_group_params import GenericNasProtectionGroupParams
    from cohesity_sdk.cluster.model.gpfs_protection_group_params import GpfsProtectionGroupParams
    from cohesity_sdk.cluster.model.hdfs_protection_group_params import HdfsProtectionGroupParams
    from cohesity_sdk.cluster.model.hyper_v_protection_group_params import HyperVProtectionGroupParams
    from cohesity_sdk.cluster.model.isilon_protection_group_params import IsilonProtectionGroupParams
    from cohesity_sdk.cluster.model.kubernetes_protection_group_params import KubernetesProtectionGroupParams
    from cohesity_sdk.cluster.model.kvm_protection_group_params import KvmProtectionGroupParams
    from cohesity_sdk.cluster.model.mongo_db_protection_group_params import MongoDBProtectionGroupParams
    from cohesity_sdk.cluster.model.mssql_protection_group_params import MSSQLProtectionGroupParams
    from cohesity_sdk.cluster.model.netapp_protection_group_params import NetappProtectionGroupParams
    from cohesity_sdk.cluster.model.nimble_protection_group_params import NimbleProtectionGroupParams
    from cohesity_sdk.cluster.model.no_sql_protection_group_params import NoSqlProtectionGroupParams
    from cohesity_sdk.cluster.model.office365_protection_group_params import Office365ProtectionGroupParams
    from cohesity_sdk.cluster.model.oracle_protection_group_params import OracleProtectionGroupParams
    from cohesity_sdk.cluster.model.physical_protection_group_params import PhysicalProtectionGroupParams
    from cohesity_sdk.cluster.model.pure_protection_group_params import PureProtectionGroupParams
    from cohesity_sdk.cluster.model.remote_adapter_protection_group_params import RemoteAdapterProtectionGroupParams
    from cohesity_sdk.cluster.model.sfdc_protection_group_params import SfdcProtectionGroupParams
    from cohesity_sdk.cluster.model.uda_protection_group_params import UdaProtectionGroupParams
    from cohesity_sdk.cluster.model.view_protection_group_params import ViewProtectionGroupParams
    from cohesity_sdk.cluster.model.vmware_protection_group_params import VmwareProtectionGroupParams
    globals()['ADProtectionGroupParams'] = ADProtectionGroupParams
    globals()['AcropolisProtectionGroupParams'] = AcropolisProtectionGroupParams
    globals()['AwsProtectionGroupParams'] = AwsProtectionGroupParams
    globals()['AzureProtectionGroupParams'] = AzureProtectionGroupParams
    globals()['CassandraProtectionGroupParams'] = CassandraProtectionGroupParams
    globals()['CreateOrUpdateProtectionGroupRequestAllOf'] = CreateOrUpdateProtectionGroupRequestAllOf
    globals()['ElastifileProtectionGroupParams'] = ElastifileProtectionGroupParams
    globals()['ExchangeProtectionGroupParams'] = ExchangeProtectionGroupParams
    globals()['FlashbladeProtectionGroupParams'] = FlashbladeProtectionGroupParams
    globals()['GcpProtectionGroupParams'] = GcpProtectionGroupParams
    globals()['GenericNasProtectionGroupParams'] = GenericNasProtectionGroupParams
    globals()['GpfsProtectionGroupParams'] = GpfsProtectionGroupParams
    globals()['HdfsProtectionGroupParams'] = HdfsProtectionGroupParams
    globals()['HyperVProtectionGroupParams'] = HyperVProtectionGroupParams
    globals()['IsilonProtectionGroupParams'] = IsilonProtectionGroupParams
    globals()['KubernetesProtectionGroupParams'] = KubernetesProtectionGroupParams
    globals()['KvmProtectionGroupParams'] = KvmProtectionGroupParams
    globals()['MSSQLProtectionGroupParams'] = MSSQLProtectionGroupParams
    globals()['MongoDBProtectionGroupParams'] = MongoDBProtectionGroupParams
    globals()['NetappProtectionGroupParams'] = NetappProtectionGroupParams
    globals()['NimbleProtectionGroupParams'] = NimbleProtectionGroupParams
    globals()['NoSqlProtectionGroupParams'] = NoSqlProtectionGroupParams
    globals()['Office365ProtectionGroupParams'] = Office365ProtectionGroupParams
    globals()['OracleProtectionGroupParams'] = OracleProtectionGroupParams
    globals()['PhysicalProtectionGroupParams'] = PhysicalProtectionGroupParams
    globals()['PureProtectionGroupParams'] = PureProtectionGroupParams
    globals()['RemoteAdapterProtectionGroupParams'] = RemoteAdapterProtectionGroupParams
    globals()['SfdcProtectionGroupParams'] = SfdcProtectionGroupParams
    globals()['UdaProtectionGroupParams'] = UdaProtectionGroupParams
    globals()['ViewProtectionGroupParams'] = ViewProtectionGroupParams
    globals()['VmwareProtectionGroupParams'] = VmwareProtectionGroupParams


class CreateOrUpdateProtectionGroupRequest69fd26ac70bd49aa801bCef08760b86f(ModelComposed):
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
            'vmware_params': (VmwareProtectionGroupParams,),  # noqa: E501
            'acropolis_params': (AcropolisProtectionGroupParams,),  # noqa: E501
            'kubernetes_params': (KubernetesProtectionGroupParams,),  # noqa: E501
            'mssql_params': (MSSQLProtectionGroupParams,),  # noqa: E501
            'oracle_params': (OracleProtectionGroupParams,),  # noqa: E501
            'view_params': (ViewProtectionGroupParams,),  # noqa: E501
            'pure_params': (PureProtectionGroupParams,),  # noqa: E501
            'nimble_params': (NimbleProtectionGroupParams,),  # noqa: E501
            'hyperv_params': (HyperVProtectionGroupParams,),  # noqa: E501
            'aws_params': (AwsProtectionGroupParams,),  # noqa: E501
            'azure_params': (AzureProtectionGroupParams,),  # noqa: E501
            'gcp_params': (GcpProtectionGroupParams,),  # noqa: E501
            'kvm_params': (KvmProtectionGroupParams,),  # noqa: E501
            'physical_params': (PhysicalProtectionGroupParams,),  # noqa: E501
            'ad_params': (ADProtectionGroupParams,),  # noqa: E501
            'office365_params': (Office365ProtectionGroupParams,),  # noqa: E501
            'netapp_params': (NetappProtectionGroupParams,),  # noqa: E501
            'generic_nas_params': (GenericNasProtectionGroupParams,),  # noqa: E501
            'isilon_params': (IsilonProtectionGroupParams,),  # noqa: E501
            'flashblade_params': (FlashbladeProtectionGroupParams,),  # noqa: E501
            'gpfs_params': (GpfsProtectionGroupParams,),  # noqa: E501
            'couchbase_params': (NoSqlProtectionGroupParams,),  # noqa: E501
            'elastifile_params': (ElastifileProtectionGroupParams,),  # noqa: E501
            'cassandra_params': (CassandraProtectionGroupParams,),  # noqa: E501
            'mongodb_params': (MongoDBProtectionGroupParams,),  # noqa: E501
            'hive_params': (NoSqlProtectionGroupParams,),  # noqa: E501
            'hdfs_params': (HdfsProtectionGroupParams,),  # noqa: E501
            'hbase_params': (NoSqlProtectionGroupParams,),  # noqa: E501
            'remote_adapter_params': (RemoteAdapterProtectionGroupParams,),  # noqa: E501
            'exchange_params': (ExchangeProtectionGroupParams,),  # noqa: E501
            'uda_params': (UdaProtectionGroupParams,),  # noqa: E501
            'sfdc_params': (SfdcProtectionGroupParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'vmware_params': 'vmwareParams',  # noqa: E501
        'acropolis_params': 'acropolisParams',  # noqa: E501
        'kubernetes_params': 'kubernetesParams',  # noqa: E501
        'mssql_params': 'mssqlParams',  # noqa: E501
        'oracle_params': 'oracleParams',  # noqa: E501
        'view_params': 'viewParams',  # noqa: E501
        'pure_params': 'pureParams',  # noqa: E501
        'nimble_params': 'nimbleParams',  # noqa: E501
        'hyperv_params': 'hypervParams',  # noqa: E501
        'aws_params': 'awsParams',  # noqa: E501
        'azure_params': 'azureParams',  # noqa: E501
        'gcp_params': 'gcpParams',  # noqa: E501
        'kvm_params': 'kvmParams',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'ad_params': 'adParams',  # noqa: E501
        'office365_params': 'office365Params',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'couchbase_params': 'couchbaseParams',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'cassandra_params': 'cassandraParams',  # noqa: E501
        'mongodb_params': 'mongodbParams',  # noqa: E501
        'hive_params': 'hiveParams',  # noqa: E501
        'hdfs_params': 'hdfsParams',  # noqa: E501
        'hbase_params': 'hbaseParams',  # noqa: E501
        'remote_adapter_params': 'remoteAdapterParams',  # noqa: E501
        'exchange_params': 'exchangeParams',  # noqa: E501
        'uda_params': 'udaParams',  # noqa: E501
        'sfdc_params': 'sfdcParams',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CreateOrUpdateProtectionGroupRequest69fd26ac70bd49aa801bCef08760b86f - a model defined in OpenAPI

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

            vmware_params (VmwareProtectionGroupParams): [optional]  # noqa: E501
            acropolis_params (AcropolisProtectionGroupParams): [optional]  # noqa: E501
            kubernetes_params (KubernetesProtectionGroupParams): [optional]  # noqa: E501
            mssql_params (MSSQLProtectionGroupParams): [optional]  # noqa: E501
            oracle_params (OracleProtectionGroupParams): [optional]  # noqa: E501
            view_params (ViewProtectionGroupParams): [optional]  # noqa: E501
            pure_params (PureProtectionGroupParams): [optional]  # noqa: E501
            nimble_params (NimbleProtectionGroupParams): [optional]  # noqa: E501
            hyperv_params (HyperVProtectionGroupParams): [optional]  # noqa: E501
            aws_params (AwsProtectionGroupParams): [optional]  # noqa: E501
            azure_params (AzureProtectionGroupParams): [optional]  # noqa: E501
            gcp_params (GcpProtectionGroupParams): [optional]  # noqa: E501
            kvm_params (KvmProtectionGroupParams): [optional]  # noqa: E501
            physical_params (PhysicalProtectionGroupParams): [optional]  # noqa: E501
            ad_params (ADProtectionGroupParams): [optional]  # noqa: E501
            office365_params (Office365ProtectionGroupParams): [optional]  # noqa: E501
            netapp_params (NetappProtectionGroupParams): [optional]  # noqa: E501
            generic_nas_params (GenericNasProtectionGroupParams): [optional]  # noqa: E501
            isilon_params (IsilonProtectionGroupParams): [optional]  # noqa: E501
            flashblade_params (FlashbladeProtectionGroupParams): [optional]  # noqa: E501
            gpfs_params (GpfsProtectionGroupParams): [optional]  # noqa: E501
            couchbase_params (NoSqlProtectionGroupParams): [optional]  # noqa: E501
            elastifile_params (ElastifileProtectionGroupParams): [optional]  # noqa: E501
            cassandra_params (CassandraProtectionGroupParams): [optional]  # noqa: E501
            mongodb_params (MongoDBProtectionGroupParams): [optional]  # noqa: E501
            hive_params (NoSqlProtectionGroupParams): [optional]  # noqa: E501
            hdfs_params (HdfsProtectionGroupParams): [optional]  # noqa: E501
            hbase_params (NoSqlProtectionGroupParams): [optional]  # noqa: E501
            remote_adapter_params (RemoteAdapterProtectionGroupParams): [optional]  # noqa: E501
            exchange_params (ExchangeProtectionGroupParams): [optional]  # noqa: E501
            uda_params (UdaProtectionGroupParams): [optional]  # noqa: E501
            sfdc_params (SfdcProtectionGroupParams): [optional]  # noqa: E501
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


        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              CreateOrUpdateProtectionGroupRequestAllOf,
          ],
          'oneOf': [
          ],
        }

