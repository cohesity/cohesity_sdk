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


class FileLevelDataLockConfig(ModelNormal):
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
        ('locking_protocol',): {
            'None': None,
            'SETREADONLY': "SetReadOnly",
            'SETATIME': "SetAtime",
        },
        ('mode',): {
            'None': None,
            'COMPLIANCE': "Compliance",
            'ENTERPRISE': "Enterprise",
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
        return {
            'auto_lock_after_duration_idle_msecs': (int, none_type,),  # noqa: E501
            'default_retention_duration_msecs': (int, none_type,),  # noqa: E501
            'expiry_timestamp_msecs': (int, none_type,),  # noqa: E501
            'locking_protocol': (str, none_type,),  # noqa: E501
            'max_retention_duration_msecs': (int, none_type,),  # noqa: E501
            'min_retention_duration_msecs': (int, none_type,),  # noqa: E501
            'mode': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'auto_lock_after_duration_idle_msecs': 'autoLockAfterDurationIdleMsecs',  # noqa: E501
        'default_retention_duration_msecs': 'defaultRetentionDurationMsecs',  # noqa: E501
        'expiry_timestamp_msecs': 'expiryTimestampMsecs',  # noqa: E501
        'locking_protocol': 'lockingProtocol',  # noqa: E501
        'max_retention_duration_msecs': 'maxRetentionDurationMsecs',  # noqa: E501
        'min_retention_duration_msecs': 'minRetentionDurationMsecs',  # noqa: E501
        'mode': 'mode',  # noqa: E501
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
        """FileLevelDataLockConfig - a model defined in OpenAPI

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

            auto_lock_after_duration_idle_msecs (int, none_type): Specifies the duration to lock a file that has not been accessed or modified (ie. has been idle) for a certain duration of time in milliseconds. Do not set if it is required to disable auto lock.. [optional]  # noqa: E501
            default_retention_duration_msecs (int, none_type): Specifies a global default retention duration for files in this view, if file lock is enabled for this view. Also, it is a required field if file lock is enabled. Set to -1 if the required default retention period is forever.. [optional]  # noqa: E501
            expiry_timestamp_msecs (int, none_type): Specifies a definite timestamp in milliseconds for retaining the file.. [optional]  # noqa: E501
            locking_protocol (str, none_type): Specifies the supported mechanisms to explicity lock a file from NFS/SMB interface. Supported locking protocols: SetReadOnly, SetAtime. 'SetReadOnly' is compatible with Isilon/Netapp behaviour. This locks the file and the retention duration is determined in this order: 1) atime, if set by user/application and within min and max retention duration. 2) Min retention duration, if set. 3) Otherwise, file is switched to expired data automatically. 'SetAtime' is compatible with Data Domain behaviour.. [optional]  # noqa: E501
            max_retention_duration_msecs (int, none_type): Specifies a maximum duration in milliseconds for which any file in this view can be retained for. Set to -1 if the required retention duration is forever. If set, it should be greater than or equal to the default retention period as well as the min retention period.. [optional]  # noqa: E501
            min_retention_duration_msecs (int, none_type): Specifies a minimum retention duration in milliseconds after a file gets locked. The file cannot be modified or deleted during this timeframe. Set to -1 if the required retention duration is forever. This should be set less than or equal to the default retention duration.. [optional]  # noqa: E501
            mode (str, none_type): Specifies the mode of file level datalock. Enterprise mode can be upgraded to Compliance mode, but Compliance mode cannot be downgraded to Enterprise mode. Compliance: This mode would disallow all user to delete/modify file or view under any condition when it 's in locked status except for deleting view when the view is empty. Enterprise: This mode would follow the rules as compliance mode for normal users. But it would allow the storage admin (1) to delete view or file anytime no matter it is in locked status or expired. (2) to rename the view (3) to bring back the retention period when it's in locked mode A lock mode of a file in a view can be in one of the following: 'Compliance': Default mode of datalock, in this mode, Data Security Admin cannot modify/delete this view when datalock is in effect. Data Security Admin can delete this view when datalock is expired. 'kEnterprise' : In this mode, Data Security Admin can change view name or delete view when datalock is in effect. Datalock in this mode can be upgraded to 'Compliance' mode.. [optional]  # noqa: E501
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


