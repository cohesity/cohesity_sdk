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
    from cohesity_sdk.cluster.model.day_schedule import DaySchedule
    from cohesity_sdk.cluster.model.hour_schedule import HourSchedule
    from cohesity_sdk.cluster.model.minute_schedule import MinuteSchedule
    from cohesity_sdk.cluster.model.month_schedule import MonthSchedule
    from cohesity_sdk.cluster.model.week_schedule import WeekSchedule
    from cohesity_sdk.cluster.model.year_schedule import YearSchedule
    globals()['DaySchedule'] = DaySchedule
    globals()['HourSchedule'] = HourSchedule
    globals()['MinuteSchedule'] = MinuteSchedule
    globals()['MonthSchedule'] = MonthSchedule
    globals()['WeekSchedule'] = WeekSchedule
    globals()['YearSchedule'] = YearSchedule


class StorageArraySnapshotSchedule(ModelNormal):
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
        ('unit',): {
            'None': None,
            'MINUTES': "Minutes",
            'HOURS': "Hours",
            'DAYS': "Days",
            'WEEKS': "Weeks",
            'MONTHS': "Months",
            'YEARS': "Years",
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
            'unit': (str, none_type,),  # noqa: E501
            'day_schedule': (DaySchedule,),  # noqa: E501
            'hour_schedule': (HourSchedule,),  # noqa: E501
            'minute_schedule': (MinuteSchedule,),  # noqa: E501
            'month_schedule': (MonthSchedule,),  # noqa: E501
            'week_schedule': (WeekSchedule,),  # noqa: E501
            'year_schedule': (YearSchedule,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'unit': 'unit',  # noqa: E501
        'day_schedule': 'daySchedule',  # noqa: E501
        'hour_schedule': 'hourSchedule',  # noqa: E501
        'minute_schedule': 'minuteSchedule',  # noqa: E501
        'month_schedule': 'monthSchedule',  # noqa: E501
        'week_schedule': 'weekSchedule',  # noqa: E501
        'year_schedule': 'yearSchedule',  # noqa: E501
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
    def __init__(self, unit, *args, **kwargs):  # noqa: E501
        """StorageArraySnapshotSchedule - a model defined in OpenAPI

        Args:
            unit (str, none_type): Specifies how often to start new Protection Group Runs of a Protection Group. <br>'Minutes' specifies that Protection Group run starts periodically after certain number of minutes specified in 'frequency' field. <br>'Hours' specifies that Protection Group run starts periodically after certain number of hours specified in 'frequency' field.

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

            day_schedule (DaySchedule): [optional]  # noqa: E501
            hour_schedule (HourSchedule): [optional]  # noqa: E501
            minute_schedule (MinuteSchedule): [optional]  # noqa: E501
            month_schedule (MonthSchedule): [optional]  # noqa: E501
            week_schedule (WeekSchedule): [optional]  # noqa: E501
            year_schedule (YearSchedule): [optional]  # noqa: E501
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


        self.unit = unit
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


