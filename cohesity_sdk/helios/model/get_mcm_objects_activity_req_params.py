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
    from cohesity_sdk.helios.model.activity_stats_params import ActivityStatsParams
    from cohesity_sdk.helios.model.archival_run_filter_params import (
        ArchivalRunFilterParams,
    )
    from cohesity_sdk.helios.model.mcm_object_identifier import McmObjectIdentifier

    globals()["ActivityStatsParams"] = ActivityStatsParams
    globals()["ArchivalRunFilterParams"] = ArchivalRunFilterParams
    globals()["McmObjectIdentifier"] = McmObjectIdentifier


class GetMcmObjectsActivityReqParams(ModelNormal):
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
        ("environments",): {
            "None": None,
            "KVMWARE": "kVMware",
            "KHYPERV": "kHyperV",
            "KAZURE": "kAzure",
            "KKVM": "kKVM",
            "KAWS": "kAWS",
            "KACROPOLIS": "kAcropolis",
            "KGCP": "kGCP",
            "KPHYSICAL": "kPhysical",
            "KPHYSICALFILES": "kPhysicalFiles",
            "KISILON": "kIsilon",
            "KNETAPP": "kNetapp",
            "KGENERICNAS": "kGenericNas",
            "KFLASHBLADE": "kFlashBlade",
            "KELASTIFILE": "kElastifile",
            "KGPFS": "kGPFS",
            "KPURE": "kPure",
            "KNIMBLE": "kNimble",
            "KSQL": "kSQL",
            "KORACLE": "kOracle",
            "KEXCHANGE": "kExchange",
            "KAD": "kAD",
            "KVIEW": "kView",
            "KO365": "kO365",
            "KHYPERFLEX": "kHyperFlex",
            "KKUBERNETES": "kKubernetes",
            "KCASSANDRA": "kCassandra",
            "KMONGODB": "kMongoDB",
            "KCOUCHBASE": "kCouchbase",
            "KHDFS": "kHdfs",
            "KHIVE": "kHive",
            "KHBASE": "kHBase",
            "KUDA": "kUDA",
            "KSFDC": "kSfdc",
        },
        ("statuses",): {
            "None": None,
            "ACCEPTED": "Accepted",
            "RUNNING": "Running",
            "CANCELED": "Canceled",
            "CANCELING": "Canceling",
            "FAILED": "Failed",
            "MISSED": "Missed",
            "SUCCEEDED": "Succeeded",
            "SUCCEEDEDWITHWARNING": "SucceededWithWarning",
            "ONHOLD": "OnHold",
            "FINALIZING": "Finalizing",
        },
        ("activity_types",): {
            "None": None,
            "BACKUPRUN": "BackupRun",
            "RESTORE": "Restore",
            "ARCHIVALRUN": "ArchivalRun",
        },
    }

    validations = {}

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
            "object_identifiers": (
                [McmObjectIdentifier],
                none_type,
            ),  # noqa: E501
            "environments": (
                [str],
                none_type,
            ),  # noqa: E501
            "statuses": (
                [str],
                none_type,
            ),  # noqa: E501
            "message_codes": (
                [str],
                none_type,
            ),  # noqa: E501
            "from_time_usecs": (
                int,
                none_type,
            ),  # noqa: E501
            "to_time_usecs": (
                int,
                none_type,
            ),  # noqa: E501
            "activity_types": (
                [str],
                none_type,
            ),  # noqa: E501
            "backup_run_params": (
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)},
                none_type,
            ),  # noqa: E501
            "archival_run_params": (ArchivalRunFilterParams,),  # noqa: E501
            "restore_params": (
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)},
                none_type,
            ),  # noqa: E501
            "is_sla_violated": (
                bool,
                none_type,
            ),  # noqa: E501
            "exclude_data": (
                bool,
                none_type,
            ),  # noqa: E501
            "exclude_stats": (
                bool,
                none_type,
            ),  # noqa: E501
            "stats_params": (ActivityStatsParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "object_identifiers": "objectIdentifiers",  # noqa: E501
        "environments": "environments",  # noqa: E501
        "statuses": "statuses",  # noqa: E501
        "message_codes": "messageCodes",  # noqa: E501
        "from_time_usecs": "fromTimeUsecs",  # noqa: E501
        "to_time_usecs": "toTimeUsecs",  # noqa: E501
        "activity_types": "activityTypes",  # noqa: E501
        "backup_run_params": "backupRunParams",  # noqa: E501
        "archival_run_params": "archivalRunParams",  # noqa: E501
        "restore_params": "restoreParams",  # noqa: E501
        "is_sla_violated": "isSlaViolated",  # noqa: E501
        "exclude_data": "excludeData",  # noqa: E501
        "exclude_stats": "excludeStats",  # noqa: E501
        "stats_params": "statsParams",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """GetMcmObjectsActivityReqParams - a model defined in OpenAPI

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

            object_identifiers ([McmObjectIdentifier], none_type): Specifies the list of object identifiers to filter the activity.. [optional]  # noqa: E501
            environments ([str], none_type): Specifies the list of environments.. [optional]  # noqa: E501
            statuses ([str], none_type): Specifies the list of statuses to filter activity events.. [optional]  # noqa: E501
            message_codes ([str], none_type): Specifies the error codes to filter backup runs.. [optional]  # noqa: E501
            from_time_usecs (int, none_type): Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started after this value.. [optional]  # noqa: E501
            to_time_usecs (int, none_type): Specifies the time in Unix timestamp epoch in microsecond which filters all the activity started before this value.. [optional]  # noqa: E501
            activity_types ([str], none_type): Specifies the activity types.. [optional]  # noqa: E501
            backup_run_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Specifies the additional filters in case activity type is set to 'BackupRun'.. [optional]  # noqa: E501
            archival_run_params (ArchivalRunFilterParams): [optional]  # noqa: E501
            restore_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Specifies the additional filters in case activity type is set to 'Restore'.. [optional]  # noqa: E501
            is_sla_violated (bool, none_type): Specifies whether to only return activities which violated SLA. Default is false.. [optional]  # noqa: E501
            exclude_data (bool, none_type): Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included.. [optional]  # noqa: E501
            exclude_stats (bool, none_type): Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included.. [optional]  # noqa: E501
            stats_params (ActivityStatsParams): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
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
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
