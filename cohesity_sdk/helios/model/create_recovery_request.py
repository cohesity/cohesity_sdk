"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.helios.model_utils import (  # noqa: F401
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
    from cohesity_sdk.helios.model.cassandra_params import CassandraParams
    from cohesity_sdk.helios.model.common_recovery_request_params import CommonRecoveryRequestParams
    from cohesity_sdk.helios.model.couchbase_params import CouchbaseParams
    from cohesity_sdk.helios.model.create_recovery_request_all_of import CreateRecoveryRequestAllOf
    from cohesity_sdk.helios.model.hbase_params import HbaseParams
    from cohesity_sdk.helios.model.hdfs_params import HdfsParams
    from cohesity_sdk.helios.model.hive_params import HiveParams
    from cohesity_sdk.helios.model.mongodb_params import MongodbParams
    from cohesity_sdk.helios.model.recover_acropolis_params import RecoverAcropolisParams
    from cohesity_sdk.helios.model.recover_aws_params import RecoverAwsParams
    from cohesity_sdk.helios.model.recover_azure_params import RecoverAzureParams
    from cohesity_sdk.helios.model.recover_elastifile_params import RecoverElastifileParams
    from cohesity_sdk.helios.model.recover_exchange_params import RecoverExchangeParams
    from cohesity_sdk.helios.model.recover_flashblade_params import RecoverFlashbladeParams
    from cohesity_sdk.helios.model.recover_gcp_params import RecoverGcpParams
    from cohesity_sdk.helios.model.recover_generic_nas_params import RecoverGenericNasParams
    from cohesity_sdk.helios.model.recover_gpfs_params import RecoverGpfsParams
    from cohesity_sdk.helios.model.recover_hyper_v_params import RecoverHyperVParams
    from cohesity_sdk.helios.model.recover_isilon_params import RecoverIsilonParams
    from cohesity_sdk.helios.model.recover_kubernetes_params import RecoverKubernetesParams
    from cohesity_sdk.helios.model.recover_kvm_params import RecoverKvmParams
    from cohesity_sdk.helios.model.recover_netapp_params import RecoverNetappParams
    from cohesity_sdk.helios.model.recover_o365_params import RecoverO365Params
    from cohesity_sdk.helios.model.recover_oracle_params import RecoverOracleParams
    from cohesity_sdk.helios.model.recover_physical_params import RecoverPhysicalParams
    from cohesity_sdk.helios.model.recover_pure_params import RecoverPureParams
    from cohesity_sdk.helios.model.recover_salesforce_params import RecoverSalesforceParams
    from cohesity_sdk.helios.model.recover_sql_params import RecoverSqlParams
    from cohesity_sdk.helios.model.recover_vmware_params import RecoverVmwareParams
    from cohesity_sdk.helios.model.uda_params import UdaParams
    globals()['CassandraParams'] = CassandraParams
    globals()['CommonRecoveryRequestParams'] = CommonRecoveryRequestParams
    globals()['CouchbaseParams'] = CouchbaseParams
    globals()['CreateRecoveryRequestAllOf'] = CreateRecoveryRequestAllOf
    globals()['HbaseParams'] = HbaseParams
    globals()['HdfsParams'] = HdfsParams
    globals()['HiveParams'] = HiveParams
    globals()['MongodbParams'] = MongodbParams
    globals()['RecoverAcropolisParams'] = RecoverAcropolisParams
    globals()['RecoverAwsParams'] = RecoverAwsParams
    globals()['RecoverAzureParams'] = RecoverAzureParams
    globals()['RecoverElastifileParams'] = RecoverElastifileParams
    globals()['RecoverExchangeParams'] = RecoverExchangeParams
    globals()['RecoverFlashbladeParams'] = RecoverFlashbladeParams
    globals()['RecoverGcpParams'] = RecoverGcpParams
    globals()['RecoverGenericNasParams'] = RecoverGenericNasParams
    globals()['RecoverGpfsParams'] = RecoverGpfsParams
    globals()['RecoverHyperVParams'] = RecoverHyperVParams
    globals()['RecoverIsilonParams'] = RecoverIsilonParams
    globals()['RecoverKubernetesParams'] = RecoverKubernetesParams
    globals()['RecoverKvmParams'] = RecoverKvmParams
    globals()['RecoverNetappParams'] = RecoverNetappParams
    globals()['RecoverO365Params'] = RecoverO365Params
    globals()['RecoverOracleParams'] = RecoverOracleParams
    globals()['RecoverPhysicalParams'] = RecoverPhysicalParams
    globals()['RecoverPureParams'] = RecoverPureParams
    globals()['RecoverSalesforceParams'] = RecoverSalesforceParams
    globals()['RecoverSqlParams'] = RecoverSqlParams
    globals()['RecoverVmwareParams'] = RecoverVmwareParams
    globals()['UdaParams'] = UdaParams


class CreateRecoveryRequest(ModelComposed):
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
        ('snapshot_environment',): {
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KAZURE': "kAzure",
            'KGCP': "kGCP",
            'KKVM': "kKVM",
            'KACROPOLIS': "kAcropolis",
            'KAWS': "kAWS",
            'KPHYSICAL': "kPhysical",
            'KGPFS': "kGPFS",
            'KELASTIFILE': "kElastifile",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KISILON': "kIsilon",
            'KFLASHBLADE': "kFlashBlade",
            'KPURE': "kPure",
            'KSQL': "kSQL",
            'KEXCHANGE': "kExchange",
            'KAD': "kAD",
            'KORACLE': "kOracle",
            'KVIEW': "kView",
            'KREMOTEADAPTER': "kRemoteAdapter",
            'KO365': "kO365",
            'KKUBERNETES': "kKubernetes",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
            'KSFDC': "kSfdc",
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
            'name': (str, none_type,),  # noqa: E501
            'snapshot_environment': (str,),  # noqa: E501
            'vmware_params': (RecoverVmwareParams,),  # noqa: E501
            'aws_params': (RecoverAwsParams,),  # noqa: E501
            'gcp_params': (RecoverGcpParams,),  # noqa: E501
            'azure_params': (RecoverAzureParams,),  # noqa: E501
            'kvm_params': (RecoverKvmParams,),  # noqa: E501
            'acropolis_params': (RecoverAcropolisParams,),  # noqa: E501
            'mssql_params': (RecoverSqlParams,),  # noqa: E501
            'netapp_params': (RecoverNetappParams,),  # noqa: E501
            'generic_nas_params': (RecoverGenericNasParams,),  # noqa: E501
            'isilon_params': (RecoverIsilonParams,),  # noqa: E501
            'flashblade_params': (RecoverFlashbladeParams,),  # noqa: E501
            'elastifile_params': (RecoverElastifileParams,),  # noqa: E501
            'gpfs_params': (RecoverGpfsParams,),  # noqa: E501
            'physical_params': (RecoverPhysicalParams,),  # noqa: E501
            'hyperv_params': (RecoverHyperVParams,),  # noqa: E501
            'exchange_params': (RecoverExchangeParams,),  # noqa: E501
            'cassandra_params': (CassandraParams,),  # noqa: E501
            'uda_params': (UdaParams,),  # noqa: E501
            'couchbase_params': (CouchbaseParams,),  # noqa: E501
            'hbase_params': (HbaseParams,),  # noqa: E501
            'hdfs_params': (HdfsParams,),  # noqa: E501
            'hive_params': (HiveParams,),  # noqa: E501
            'mongodb_params': (MongodbParams,),  # noqa: E501
            'pure_params': (RecoverPureParams,),  # noqa: E501
            'kubernetes_params': (RecoverKubernetesParams,),  # noqa: E501
            'office365_params': (RecoverO365Params,),  # noqa: E501
            'oracle_params': (RecoverOracleParams,),  # noqa: E501
            'sfdc_params': (RecoverSalesforceParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'snapshot_environment': 'snapshotEnvironment',  # noqa: E501
        'vmware_params': 'vmwareParams',  # noqa: E501
        'aws_params': 'awsParams',  # noqa: E501
        'gcp_params': 'gcpParams',  # noqa: E501
        'azure_params': 'azureParams',  # noqa: E501
        'kvm_params': 'kvmParams',  # noqa: E501
        'acropolis_params': 'acropolisParams',  # noqa: E501
        'mssql_params': 'mssqlParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'hyperv_params': 'hypervParams',  # noqa: E501
        'exchange_params': 'exchangeParams',  # noqa: E501
        'cassandra_params': 'cassandraParams',  # noqa: E501
        'uda_params': 'udaParams',  # noqa: E501
        'couchbase_params': 'couchbaseParams',  # noqa: E501
        'hbase_params': 'hbaseParams',  # noqa: E501
        'hdfs_params': 'hdfsParams',  # noqa: E501
        'hive_params': 'hiveParams',  # noqa: E501
        'mongodb_params': 'mongodbParams',  # noqa: E501
        'pure_params': 'pureParams',  # noqa: E501
        'kubernetes_params': 'kubernetesParams',  # noqa: E501
        'office365_params': 'office365Params',  # noqa: E501
        'oracle_params': 'oracleParams',  # noqa: E501
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
    def __init__(self, name, snapshot_environment, *args, **kwargs):  # noqa: E501
        """CreateRecoveryRequest - a model defined in OpenAPI

        Args:
            name (str, none_type): Specifies the name of the Recovery.
            snapshot_environment (str): Specifies the type of environment of snapshots for which the Recovery has to be performed.

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

            vmware_params (RecoverVmwareParams): [optional]  # noqa: E501
            aws_params (RecoverAwsParams): [optional]  # noqa: E501
            gcp_params (RecoverGcpParams): [optional]  # noqa: E501
            azure_params (RecoverAzureParams): [optional]  # noqa: E501
            kvm_params (RecoverKvmParams): [optional]  # noqa: E501
            acropolis_params (RecoverAcropolisParams): [optional]  # noqa: E501
            mssql_params (RecoverSqlParams): [optional]  # noqa: E501
            netapp_params (RecoverNetappParams): [optional]  # noqa: E501
            generic_nas_params (RecoverGenericNasParams): [optional]  # noqa: E501
            isilon_params (RecoverIsilonParams): [optional]  # noqa: E501
            flashblade_params (RecoverFlashbladeParams): [optional]  # noqa: E501
            elastifile_params (RecoverElastifileParams): [optional]  # noqa: E501
            gpfs_params (RecoverGpfsParams): [optional]  # noqa: E501
            physical_params (RecoverPhysicalParams): [optional]  # noqa: E501
            hyperv_params (RecoverHyperVParams): [optional]  # noqa: E501
            exchange_params (RecoverExchangeParams): [optional]  # noqa: E501
            cassandra_params (CassandraParams): [optional]  # noqa: E501
            uda_params (UdaParams): [optional]  # noqa: E501
            couchbase_params (CouchbaseParams): [optional]  # noqa: E501
            hbase_params (HbaseParams): [optional]  # noqa: E501
            hdfs_params (HdfsParams): [optional]  # noqa: E501
            hive_params (HiveParams): [optional]  # noqa: E501
            mongodb_params (MongodbParams): [optional]  # noqa: E501
            pure_params (RecoverPureParams): [optional]  # noqa: E501
            kubernetes_params (RecoverKubernetesParams): [optional]  # noqa: E501
            office365_params (RecoverO365Params): [optional]  # noqa: E501
            oracle_params (RecoverOracleParams): [optional]  # noqa: E501
            sfdc_params (RecoverSalesforceParams): [optional]  # noqa: E501
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
            'name': name,
            'snapshot_environment': snapshot_environment,
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
              CommonRecoveryRequestParams,
              CreateRecoveryRequestAllOf,
          ],
          'oneOf': [
          ],
        }

