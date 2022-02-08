"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cohesity_sdk.cohesity_client_v2.model_utils import (  # noqa: F401
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
    from cohesity_sdk.cohesity_client_v2.model.common_recovery_request_params6cc0a9973f4b47a8_a51f_bdda823aab75_hbase_params_wrapper_all_of import CommonRecoveryRequestParams6cc0a9973f4b47a8A51fBdda823aab75HbaseParamsWrapperAllOf
    from cohesity_sdk.cohesity_client_v2.model.common_recovery_response_params8c60ab25210e4ab097394c9e12eb86fb import CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fb
    from cohesity_sdk.cohesity_client_v2.model.creation_info import CreationInfo
    from cohesity_sdk.cohesity_client_v2.model.hbase_params import HbaseParams
    from cohesity_sdk.cohesity_client_v2.model.tenant import Tenant
    globals()['CommonRecoveryRequestParams6cc0a9973f4b47a8A51fBdda823aab75HbaseParamsWrapperAllOf'] = CommonRecoveryRequestParams6cc0a9973f4b47a8A51fBdda823aab75HbaseParamsWrapperAllOf
    globals()['CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fb'] = CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fb
    globals()['CreationInfo'] = CreationInfo
    globals()['HbaseParams'] = HbaseParams
    globals()['Tenant'] = Tenant


class CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fbHbaseParamsWrapper(ModelComposed):
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
        ('status',): {
            'None': None,
            'ACCEPTED': "Accepted",
            'RUNNING': "Running",
            'CANCELED': "Canceled",
            'CANCELING': "Canceling",
            'FAILED': "Failed",
            'MISSED': "Missed",
            'SUCCEEDED': "Succeeded",
            'SUCCEEDEDWITHWARNING': "SucceededWithWarning",
            'ONHOLD': "OnHold",
        },
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
        },
        ('recovery_action',): {
            'RECOVERVMS': "RecoverVMs",
            'RECOVERFILES': "RecoverFiles",
            'INSTANTVOLUMEMOUNT': "InstantVolumeMount",
            'RECOVERVMDISKS': "RecoverVmDisks",
            'RECOVERVAPPS': "RecoverVApps",
            'RECOVERVAPPTEMPLATES': "RecoverVAppTemplates",
            'RECOVERRDS': "RecoverRDS",
            'RECOVERAURORA': "RecoverAurora",
            'RECOVERAPPS': "RecoverApps",
            'RECOVERNASVOLUME': "RecoverNasVolume",
            'RECOVERPHYSICALVOLUMES': "RecoverPhysicalVolumes",
            'RECOVERSYSTEM': "RecoverSystem",
            'CLONEAPPVIEW': "CloneAppView",
            'RECOVERSANVOLUMES': "RecoverSanVolumes",
            'RECOVERMAILBOX': "RecoverMailbox",
            'RECOVERONEDRIVE': "RecoverOneDrive",
            'RECOVERSHAREPOINT': "RecoverSharePoint",
            'RECOVERPUBLICFOLDERS': "RecoverPublicFolders",
            'RECOVERMSGROUP': "RecoverMsGroup",
            'RECOVERMSTEAM': "RecoverMsTeam",
            'CONVERTTOPST': "ConvertToPst",
            'RECOVERNAMESPACES': "RecoverNamespaces",
            'RECOVEROBJECTS': "RecoverObjects",
            'DOWNLOADFILESANDFOLDERS': "DownloadFilesAndFolders",
        },
        ('tear_down_status',): {
            'None': None,
            'DESTROYSCHEDULED': "DestroyScheduled",
            'DESTROYING': "Destroying",
            'DESTROYED': "Destroyed",
            'DESTROYERROR': "DestroyError",
        },
    }

    validations = {
        ('id',): {
            'regex': {
                'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
            },
        },

        ('parent_recovery_id',): {
            'regex': {
                'pattern': r'^\d+:\d+:\d+$',  # noqa: E501
            },
        },

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
            'name': (str, none_type,),  # noqa: E501
            'start_time_usecs': (int, none_type,),  # noqa: E501
            'end_time_usecs': (int, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'progress_task_id': (str, none_type,),  # noqa: E501
            'snapshot_environment': (str,),  # noqa: E501
            'recovery_action': (str,),  # noqa: E501
            'permissions': ([Tenant], none_type,),  # noqa: E501
            'creation_info': (CreationInfo,),  # noqa: E501
            'can_tear_down': (bool, none_type,),  # noqa: E501
            'tear_down_status': (str, none_type,),  # noqa: E501
            'tear_down_message': (str, none_type,),  # noqa: E501
            'messages': ([str], none_type,),  # noqa: E501
            'is_parent_recovery': (bool, none_type,),  # noqa: E501
            'parent_recovery_id': (str, none_type,),  # noqa: E501
            'hbase_params': (HbaseParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'start_time_usecs': 'startTimeUsecs',  # noqa: E501
        'end_time_usecs': 'endTimeUsecs',  # noqa: E501
        'status': 'status',  # noqa: E501
        'progress_task_id': 'progressTaskId',  # noqa: E501
        'snapshot_environment': 'snapshotEnvironment',  # noqa: E501
        'recovery_action': 'recoveryAction',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'creation_info': 'creationInfo',  # noqa: E501
        'can_tear_down': 'canTearDown',  # noqa: E501
        'tear_down_status': 'tearDownStatus',  # noqa: E501
        'tear_down_message': 'tearDownMessage',  # noqa: E501
        'messages': 'messages',  # noqa: E501
        'is_parent_recovery': 'isParentRecovery',  # noqa: E501
        'parent_recovery_id': 'parentRecoveryId',  # noqa: E501
        'hbase_params': 'hbaseParams',  # noqa: E501
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
        """CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fbHbaseParamsWrapper - a model defined in OpenAPI

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

            id (str, none_type): Specifies the id of the Recovery.. [optional]  # noqa: E501
            name (str, none_type): Specifies the name of the Recovery.. [optional]  # noqa: E501
            start_time_usecs (int, none_type): Specifies the start time of the Recovery in Unix timestamp epoch in microseconds.. [optional]  # noqa: E501
            end_time_usecs (int, none_type): Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished.. [optional]  # noqa: E501
            status (str, none_type): Status of the Recovery. 'Running' indicates that the Recovery is still running. 'Canceled' indicates that the Recovery has been cancelled. 'Canceling' indicates that the Recovery is in the process of being cancelled. 'Failed' indicates that the Recovery has failed. 'Succeeded' indicates that the Recovery has finished successfully. 'SucceededWithWarning' indicates that the Recovery finished successfully, but there were some warning messages.. [optional]  # noqa: E501
            progress_task_id (str, none_type): Progress monitor task id for Recovery.. [optional]  # noqa: E501
            snapshot_environment (str): Specifies the type of snapshot environment for which the Recovery was performed.. [optional]  # noqa: E501
            recovery_action (str): Specifies the type of recover action.. [optional]  # noqa: E501
            permissions ([Tenant], none_type): Specifies the list of tenants that have permissions for this recovery.. [optional]  # noqa: E501
            creation_info (CreationInfo): [optional]  # noqa: E501
            can_tear_down (bool, none_type): Specifies whether it's possible to tear down the objects created by the recovery.. [optional]  # noqa: E501
            tear_down_status (str, none_type): Specifies the status of the tear down operation. This is only set when the canTearDown is set to true. 'DestroyScheduled' indicates that the tear down is ready to schedule. 'Destroying' indicates that the tear down is still running. 'Destroyed' indicates that the tear down succeeded. 'DestroyError' indicates that the tear down failed.. [optional]  # noqa: E501
            tear_down_message (str, none_type): Specifies the error message about the tear down operation if it fails.. [optional]  # noqa: E501
            messages ([str], none_type): Specifies messages about the recovery.. [optional]  # noqa: E501
            is_parent_recovery (bool, none_type): Specifies whether the current recovery operation has created child recoveries. This is currently used in SQL recovery where multiple child recoveries can be tracked under a common/parent recovery.. [optional]  # noqa: E501
            parent_recovery_id (str, none_type): If current recovery is child recovery triggered by another parent recovery operation, then this field willt specify the id of the parent recovery.. [optional]  # noqa: E501
            hbase_params (HbaseParams): [optional]  # noqa: E501
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
              CommonRecoveryRequestParams6cc0a9973f4b47a8A51fBdda823aab75HbaseParamsWrapperAllOf,
              CommonRecoveryResponseParams8c60ab25210e4ab097394c9e12eb86fb,
          ],
          'oneOf': [
          ],
        }

