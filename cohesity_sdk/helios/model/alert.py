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
    from cohesity_sdk.helios.model.alert_document import AlertDocument
    globals()['AlertDocument'] = AlertDocument


class Alert(ModelNormal):
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
        ('alert_type_bucket',): {
            'None': None,
            'KHARDWARE': "kHardware",
            'KSOFTWARE': "kSoftware",
            'KDATASERVICE': "kDataService",
            'KMAINTENANCE': "kMaintenance",
        },
        ('alert_category',): {
            'None': None,
            'KDISK': "kDisk",
            'KNODE': "kNode",
            'KCLUSTER': "kCluster",
            'KCHASSIS': "kChassis",
            'KPOWERSUPPLY': "kPowerSupply",
            'KCPU': "kCPU",
            'KMEMORY': "kMemory",
            'KTEMPERATURE': "kTemperature",
            'KFAN': "kFan",
            'KNIC': "kNIC",
            'KFIRMWARE': "kFirmware",
            'KNODEHEALTH': "kNodeHealth",
            'KOPERATINGSYSTEM': "kOperatingSystem",
            'KDATAPATH': "kDataPath",
            'KMETADATA': "kMetadata",
            'KINDEXING': "kIndexing",
            'KHELIOS': "kHelios",
            'KAPPMARKETPLACE': "kAppMarketPlace",
            'KSYSTEMSERVICE': "kSystemService",
            'KLICENSE': "kLicense",
            'KSECURITY': "kSecurity",
            'KUPGRADE': "kUpgrade",
            'KCLUSTERMANAGEMENT': "kClusterManagement",
            'KAUDITLOG': "kAuditLog",
            'KNETWORKING': "kNetworking",
            'KCONFIGURATION': "kConfiguration",
            'KSTORAGEUSAGE': "kStorageUsage",
            'KFAULTTOLERANCE': "kFaultTolerance",
            'KBACKUPRESTORE': "kBackupRestore",
            'KARCHIVALRESTORE': "kArchivalRestore",
            'KREMOTEREPLICATION': "kRemoteReplication",
            'KQUOTA': "kQuota",
            'KCDP': "kCDP",
            'KVIEWFAILOVER': "kViewFailover",
            'KDISASTERRECOVERY': "kDisasterRecovery",
        },
        ('severity',): {
            'None': None,
            'KCRITICAL': "kCritical",
            'KWARNING': "kWarning",
            'KINFO': "kInfo",
        },
        ('alert_state',): {
            'None': None,
            'KRESOLVED': "kResolved",
            'KOPEN': "kOpen",
            'KNOTE': "kNote",
            'KSUPPRESSED': "kSuppressed",
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
            'id': (str, none_type,),  # noqa: E501
            'alert_code': (str, none_type,),  # noqa: E501
            'first_timestamp_usecs': (int, none_type,),  # noqa: E501
            'latest_timestamp_usecs': (int, none_type,),  # noqa: E501
            'alert_type': (int, none_type,),  # noqa: E501
            'dedup_timestamps': ([int], none_type,),  # noqa: E501
            'dedup_count': (int, none_type,),  # noqa: E501
            'cluster_name': (str, none_type,),  # noqa: E501
            'region_id': (str, none_type,),  # noqa: E501
            'alert_type_bucket': (str, none_type,),  # noqa: E501
            'alert_category': (str, none_type,),  # noqa: E501
            'severity': (str, none_type,),  # noqa: E501
            'alert_state': (str, none_type,),  # noqa: E501
            'alert_document': (AlertDocument,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'alert_code': 'alertCode',  # noqa: E501
        'first_timestamp_usecs': 'firstTimestampUsecs',  # noqa: E501
        'latest_timestamp_usecs': 'latestTimestampUsecs',  # noqa: E501
        'alert_type': 'alertType',  # noqa: E501
        'dedup_timestamps': 'dedupTimestamps',  # noqa: E501
        'dedup_count': 'dedupCount',  # noqa: E501
        'cluster_name': 'clusterName',  # noqa: E501
        'region_id': 'regionId',  # noqa: E501
        'alert_type_bucket': 'alertTypeBucket',  # noqa: E501
        'alert_category': 'alertCategory',  # noqa: E501
        'severity': 'severity',  # noqa: E501
        'alert_state': 'alertState',  # noqa: E501
        'alert_document': 'alertDocument',  # noqa: E501
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
        """Alert - a model defined in OpenAPI

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

            id (str, none_type): Specifies unique id of the alert.. [optional]  # noqa: E501
            alert_code (str, none_type): Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the alert state next 3 digits is the id of the Alert Category (e.g. 002 for 'kNode') and the last 5 digits is the id of the Alert Type (e.g. 00014 for 'kNodeHighCpuUsage').. [optional]  # noqa: E501
            first_timestamp_usecs (int, none_type): SpeSpecifies Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert.. [optional]  # noqa: E501
            latest_timestamp_usecs (int, none_type): SpeSpecifies Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert.. [optional]  # noqa: E501
            alert_type (int, none_type): Specifies the alert type.. [optional]  # noqa: E501
            dedup_timestamps ([int], none_type): Specifies Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. 'dedupCount' always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100.. [optional]  # noqa: E501
            dedup_count (int, none_type): Specifies the dedup count of alert.. [optional]  # noqa: E501
            cluster_name (str, none_type): Specifies the name of cluster which alert is raised from.. [optional]  # noqa: E501
            region_id (str, none_type): Specifies the region id of the alert.. [optional]  # noqa: E501
            alert_type_bucket (str, none_type): Specifies the Alert type bucket.. [optional]  # noqa: E501
            alert_category (str, none_type): Specifies the alert category.. [optional]  # noqa: E501
            severity (str, none_type): Specifies the alert severity.. [optional]  # noqa: E501
            alert_state (str, none_type): Specifies the alert state.. [optional]  # noqa: E501
            alert_document (AlertDocument): [optional]  # noqa: E501
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


