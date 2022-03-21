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
    from cohesity_sdk.helios.model.aws_source_registration_params import AwsSourceRegistrationParams
    from cohesity_sdk.helios.model.cassandra_source_registration_params import CassandraSourceRegistrationParams
    from cohesity_sdk.helios.model.common_source_registration_reponse_params import CommonSourceRegistrationReponseParams
    from cohesity_sdk.helios.model.connection_config import ConnectionConfig
    from cohesity_sdk.helios.model.couchbase_source_registration_params import CouchbaseSourceRegistrationParams
    from cohesity_sdk.helios.model.elastifile_registration_params import ElastifileRegistrationParams
    from cohesity_sdk.helios.model.flashblade_registration_params import FlashbladeRegistrationParams
    from cohesity_sdk.helios.model.generic_nas_registration_params import GenericNasRegistrationParams
    from cohesity_sdk.helios.model.gpfs_registration_params import GpfsRegistrationParams
    from cohesity_sdk.helios.model.hbase_source_registration_params import HbaseSourceRegistrationParams
    from cohesity_sdk.helios.model.hdfs_source_registration_params import HdfsSourceRegistrationParams
    from cohesity_sdk.helios.model.hive_source_registration_params import HiveSourceRegistrationParams
    from cohesity_sdk.helios.model.hyper_v_source_registration_params import HyperVSourceRegistrationParams
    from cohesity_sdk.helios.model.isilon_registration_params import IsilonRegistrationParams
    from cohesity_sdk.helios.model.mongo_db_source_registration_params import MongoDBSourceRegistrationParams
    from cohesity_sdk.helios.model.netapp_registration_params import NetappRegistrationParams
    from cohesity_sdk.helios.model.object import Object
    from cohesity_sdk.helios.model.office365_source_registration_params import Office365SourceRegistrationParams
    from cohesity_sdk.helios.model.physical_source_registration_params import PhysicalSourceRegistrationParams
    from cohesity_sdk.helios.model.sfdc_source_registration_params import SfdcSourceRegistrationParams
    from cohesity_sdk.helios.model.source_registration_all_of import SourceRegistrationAllOf
    from cohesity_sdk.helios.model.uda_source_registration_params import UdaSourceRegistrationParams
    from cohesity_sdk.helios.model.vmware_source_registration_params import VmwareSourceRegistrationParams
    globals()['AwsSourceRegistrationParams'] = AwsSourceRegistrationParams
    globals()['CassandraSourceRegistrationParams'] = CassandraSourceRegistrationParams
    globals()['CommonSourceRegistrationReponseParams'] = CommonSourceRegistrationReponseParams
    globals()['ConnectionConfig'] = ConnectionConfig
    globals()['CouchbaseSourceRegistrationParams'] = CouchbaseSourceRegistrationParams
    globals()['ElastifileRegistrationParams'] = ElastifileRegistrationParams
    globals()['FlashbladeRegistrationParams'] = FlashbladeRegistrationParams
    globals()['GenericNasRegistrationParams'] = GenericNasRegistrationParams
    globals()['GpfsRegistrationParams'] = GpfsRegistrationParams
    globals()['HbaseSourceRegistrationParams'] = HbaseSourceRegistrationParams
    globals()['HdfsSourceRegistrationParams'] = HdfsSourceRegistrationParams
    globals()['HiveSourceRegistrationParams'] = HiveSourceRegistrationParams
    globals()['HyperVSourceRegistrationParams'] = HyperVSourceRegistrationParams
    globals()['IsilonRegistrationParams'] = IsilonRegistrationParams
    globals()['MongoDBSourceRegistrationParams'] = MongoDBSourceRegistrationParams
    globals()['NetappRegistrationParams'] = NetappRegistrationParams
    globals()['Object'] = Object
    globals()['Office365SourceRegistrationParams'] = Office365SourceRegistrationParams
    globals()['PhysicalSourceRegistrationParams'] = PhysicalSourceRegistrationParams
    globals()['SfdcSourceRegistrationParams'] = SfdcSourceRegistrationParams
    globals()['SourceRegistrationAllOf'] = SourceRegistrationAllOf
    globals()['UdaSourceRegistrationParams'] = UdaSourceRegistrationParams
    globals()['VmwareSourceRegistrationParams'] = VmwareSourceRegistrationParams


class SourceRegistration(ModelComposed):
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
        ('environment',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KACROPOLIS': "kAcropolis",
            'KKVM': "kKVM",
            'KAWS': "kAWS",
            'KGCP': "kGCP",
            'KAZURE': "kAzure",
            'KPHYSICAL': "kPhysical",
            'KPURE': "kPure",
            'KNIMBLE': "kNimble",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KISILON': "kIsilon",
            'KFLASHBLADE': "kFlashBlade",
            'KGPFS': "kGPFS",
            'KELASTIFILE': "kElastifile",
            'KO365': "kO365",
            'KHYPERFLEX': "kHyperFlex",
            'KKUBERNETES': "kKubernetes",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
            'KSQL': "kSQL",
            'KORACLE': "kOracle",
            'KSFDC': "kSfdc",
        },
        ('authentication_status',): {
            'None': None,
            'PENDING': "Pending",
            'SCHEDULED': "Scheduled",
            'FINISHED': "Finished",
            'REFRESHINPROGRESS': "RefreshInProgress",
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
            'id': (int, none_type,),  # noqa: E501
            'source_id': (int, none_type,),  # noqa: E501
            'source_info': (Object,),  # noqa: E501
            'environment': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'connection_id': (int, none_type,),  # noqa: E501
            'connections': ([ConnectionConfig], none_type,),  # noqa: E501
            'connector_group_id': (int, none_type,),  # noqa: E501
            'authentication_status': (str, none_type,),  # noqa: E501
            'registration_time_msecs': (int, none_type,),  # noqa: E501
            'last_refreshed_time_msecs': (int, none_type,),  # noqa: E501
            'vmware_params': (VmwareSourceRegistrationParams,),  # noqa: E501
            'physical_params': (PhysicalSourceRegistrationParams,),  # noqa: E501
            'generic_nas_params': (GenericNasRegistrationParams,),  # noqa: E501
            'isilon_params': (IsilonRegistrationParams,),  # noqa: E501
            'netapp_params': (NetappRegistrationParams,),  # noqa: E501
            'elastifile_params': (ElastifileRegistrationParams,),  # noqa: E501
            'flashblade_params': (FlashbladeRegistrationParams,),  # noqa: E501
            'gpfs_params': (GpfsRegistrationParams,),  # noqa: E501
            'cassandra_params': (CassandraSourceRegistrationParams,),  # noqa: E501
            'mongodb_params': (MongoDBSourceRegistrationParams,),  # noqa: E501
            'couchbase_params': (CouchbaseSourceRegistrationParams,),  # noqa: E501
            'hdfs_params': (HdfsSourceRegistrationParams,),  # noqa: E501
            'hbase_params': (HbaseSourceRegistrationParams,),  # noqa: E501
            'hive_params': (HiveSourceRegistrationParams,),  # noqa: E501
            'uda_params': (UdaSourceRegistrationParams,),  # noqa: E501
            'office365_params': (Office365SourceRegistrationParams,),  # noqa: E501
            'aws_params': (AwsSourceRegistrationParams,),  # noqa: E501
            'hyperv_params': (HyperVSourceRegistrationParams,),  # noqa: E501
            'sfdc_params': (SfdcSourceRegistrationParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'source_info': 'sourceInfo',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'name': 'name',  # noqa: E501
        'connection_id': 'connectionId',  # noqa: E501
        'connections': 'connections',  # noqa: E501
        'connector_group_id': 'connectorGroupId',  # noqa: E501
        'authentication_status': 'authenticationStatus',  # noqa: E501
        'registration_time_msecs': 'registrationTimeMsecs',  # noqa: E501
        'last_refreshed_time_msecs': 'lastRefreshedTimeMsecs',  # noqa: E501
        'vmware_params': 'vmwareParams',  # noqa: E501
        'physical_params': 'physicalParams',  # noqa: E501
        'generic_nas_params': 'genericNasParams',  # noqa: E501
        'isilon_params': 'isilonParams',  # noqa: E501
        'netapp_params': 'netappParams',  # noqa: E501
        'elastifile_params': 'elastifileParams',  # noqa: E501
        'flashblade_params': 'flashbladeParams',  # noqa: E501
        'gpfs_params': 'gpfsParams',  # noqa: E501
        'cassandra_params': 'cassandraParams',  # noqa: E501
        'mongodb_params': 'mongodbParams',  # noqa: E501
        'couchbase_params': 'couchbaseParams',  # noqa: E501
        'hdfs_params': 'hdfsParams',  # noqa: E501
        'hbase_params': 'hbaseParams',  # noqa: E501
        'hive_params': 'hiveParams',  # noqa: E501
        'uda_params': 'udaParams',  # noqa: E501
        'office365_params': 'office365Params',  # noqa: E501
        'aws_params': 'awsParams',  # noqa: E501
        'hyperv_params': 'hypervParams',  # noqa: E501
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
        """SourceRegistration - a model defined in OpenAPI

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

            id (int, none_type): Source Registration ID. This can be used to retrieve, edit or delete the source registration.. [optional]  # noqa: E501
            source_id (int, none_type): ID of top level source object discovered after the registration.. [optional]  # noqa: E501
            source_info (Object): [optional]  # noqa: E501
            environment (str, none_type): Specifies the environment type of the Protection Source.. [optional]  # noqa: E501
            name (str, none_type): The user specified name for this source.. [optional]  # noqa: E501
            connection_id (int, none_type): Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be depricated in future. Use connections field.. [optional]  # noqa: E501
            connections ([ConnectionConfig], none_type): Specfies the list of connections for the source.. [optional]  # noqa: E501
            connector_group_id (int, none_type): Specifies the connector group id of connector groups.. [optional]  # noqa: E501
            authentication_status (str, none_type): Specifies the status of the authentication during the registration of a Protection Source. 'Pending' indicates the authentication is in progress. 'Scheduled' indicates the authentication is scheduled. 'Finished' indicates the authentication is completed. 'RefreshInProgress' indicates the refresh is in progress.. [optional]  # noqa: E501
            registration_time_msecs (int, none_type): Specifies the time when the source was registered in milliseconds. [optional]  # noqa: E501
            last_refreshed_time_msecs (int, none_type): Specifies the time when the source was last refreshed in milliseconds.. [optional]  # noqa: E501
            vmware_params (VmwareSourceRegistrationParams): [optional]  # noqa: E501
            physical_params (PhysicalSourceRegistrationParams): [optional]  # noqa: E501
            generic_nas_params (GenericNasRegistrationParams): [optional]  # noqa: E501
            isilon_params (IsilonRegistrationParams): [optional]  # noqa: E501
            netapp_params (NetappRegistrationParams): [optional]  # noqa: E501
            elastifile_params (ElastifileRegistrationParams): [optional]  # noqa: E501
            flashblade_params (FlashbladeRegistrationParams): [optional]  # noqa: E501
            gpfs_params (GpfsRegistrationParams): [optional]  # noqa: E501
            cassandra_params (CassandraSourceRegistrationParams): [optional]  # noqa: E501
            mongodb_params (MongoDBSourceRegistrationParams): [optional]  # noqa: E501
            couchbase_params (CouchbaseSourceRegistrationParams): [optional]  # noqa: E501
            hdfs_params (HdfsSourceRegistrationParams): [optional]  # noqa: E501
            hbase_params (HbaseSourceRegistrationParams): [optional]  # noqa: E501
            hive_params (HiveSourceRegistrationParams): [optional]  # noqa: E501
            uda_params (UdaSourceRegistrationParams): [optional]  # noqa: E501
            office365_params (Office365SourceRegistrationParams): [optional]  # noqa: E501
            aws_params (AwsSourceRegistrationParams): [optional]  # noqa: E501
            hyperv_params (HyperVSourceRegistrationParams): [optional]  # noqa: E501
            sfdc_params (SfdcSourceRegistrationParams): [optional]  # noqa: E501
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
              CommonSourceRegistrationReponseParams,
              SourceRegistrationAllOf,
          ],
          'oneOf': [
          ],
        }

