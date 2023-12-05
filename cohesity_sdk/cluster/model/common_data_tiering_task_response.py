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
    from cohesity_sdk.cluster.model.data_tiering_schedule import DataTieringSchedule
    from cohesity_sdk.cluster.model.data_tiering_source import DataTieringSource
    from cohesity_sdk.cluster.model.data_tiering_target import DataTieringTarget
    from cohesity_sdk.cluster.model.data_tiering_task_run import DataTieringTaskRun
    from cohesity_sdk.cluster.model.protection_group_alerting_policy import ProtectionGroupAlertingPolicy
    globals()['DataTieringSchedule'] = DataTieringSchedule
    globals()['DataTieringSource'] = DataTieringSource
    globals()['DataTieringTarget'] = DataTieringTarget
    globals()['DataTieringTaskRun'] = DataTieringTaskRun
    globals()['ProtectionGroupAlertingPolicy'] = ProtectionGroupAlertingPolicy


class CommonDataTieringTaskResponse(ModelNormal):
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
        ('type',): {
            'None': None,
            'DOWNTIER': "Downtier",
            'UPTIER': "Uptier",
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
            'type': (str, none_type,),  # noqa: E501
            'alert_policy': (ProtectionGroupAlertingPolicy,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'is_active': (bool, none_type,),  # noqa: E501
            'is_deleted': (bool, none_type,),  # noqa: E501
            'is_paused': (bool, none_type,),  # noqa: E501
            'last_run': (DataTieringTaskRun,),  # noqa: E501
            'schedule': (DataTieringSchedule,),  # noqa: E501
            'source': (DataTieringSource,),  # noqa: E501
            'target': (DataTieringTarget,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'name': 'name',  # noqa: E501
        'type': 'type',  # noqa: E501
        'alert_policy': 'alertPolicy',  # noqa: E501
        'description': 'description',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_active': 'isActive',  # noqa: E501
        'is_deleted': 'isDeleted',  # noqa: E501
        'is_paused': 'isPaused',  # noqa: E501
        'last_run': 'lastRun',  # noqa: E501
        'schedule': 'schedule',  # noqa: E501
        'source': 'source',  # noqa: E501
        'target': 'target',  # noqa: E501
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
    def __init__(self, name, type, *args, **kwargs):  # noqa: E501
        """CommonDataTieringTaskResponse - a model defined in OpenAPI

        Args:
            name (str, none_type): Specifies the name of the data tiering task.
            type (str, none_type): Type of data tiering task. 'Downtier' indicates downtiering task. 'Uptier' indicates uptiering task.

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

            alert_policy (ProtectionGroupAlertingPolicy): [optional]  # noqa: E501
            description (str, none_type): Specifies a description of the data tiering task.. [optional]  # noqa: E501
            id (str, none_type): Specifies the id of the data tiering task.. [optional]  # noqa: E501
            is_active (bool, none_type): Whether the data tiering task is active or not.. [optional] if omitted the server will use the default value of True  # noqa: E501
            is_deleted (bool, none_type): Tracks whether the backup job has actually been deleted.. [optional] if omitted the server will use the default value of True  # noqa: E501
            is_paused (bool, none_type): Whether the data tiering task is paused. New runs are not scheduled for the paused tasks. Active run of the task (if any) is not impacted.. [optional] if omitted the server will use the default value of True  # noqa: E501
            last_run (DataTieringTaskRun): [optional]  # noqa: E501
            schedule (DataTieringSchedule): [optional]  # noqa: E501
            source (DataTieringSource): [optional]  # noqa: E501
            target (DataTieringTarget): [optional]  # noqa: E501
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


        self.name = name
        self.type = type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


