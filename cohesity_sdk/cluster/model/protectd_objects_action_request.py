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
    from cohesity_sdk.cluster.model.protected_object_pause_action_params import ProtectedObjectPauseActionParams
    from cohesity_sdk.cluster.model.protected_object_resume_action_params import ProtectedObjectResumeActionParams
    from cohesity_sdk.cluster.model.protected_object_run_now_action_params import ProtectedObjectRunNowActionParams
    from cohesity_sdk.cluster.model.protected_object_un_protect_action_params import ProtectedObjectUnProtectActionParams
    globals()['ProtectedObjectPauseActionParams'] = ProtectedObjectPauseActionParams
    globals()['ProtectedObjectResumeActionParams'] = ProtectedObjectResumeActionParams
    globals()['ProtectedObjectRunNowActionParams'] = ProtectedObjectRunNowActionParams
    globals()['ProtectedObjectUnProtectActionParams'] = ProtectedObjectUnProtectActionParams


class ProtectdObjectsActionRequest(ModelNormal):
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
        ('action',): {
            'PAUSE': "Pause",
            'RESUME': "Resume",
            'UNPROTECT': "UnProtect",
            'PROTECTNOW': "ProtectNow",
        },
        ('object_action_key',): {
            'None': None,
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KVCD': "kVCD",
            'KAZURE': "kAzure",
            'KGCP': "kGCP",
            'KKVM': "kKVM",
            'KACROPOLIS': "kAcropolis",
            'KAWS': "kAWS",
            'KAWSNATIVE': "kAWSNative",
            'KAWSS3': "kAwsS3",
            'KAWSSNAPSHOTMANAGER': "kAWSSnapshotManager",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KAWSRDSPOSTGRESBACKUP': "kAwsRDSPostgresBackup",
            'KAZURENATIVE': "kAzureNative",
            'KAZURESQL': "kAzureSQL",
            'KAZURESNAPSHOTMANAGER': "kAzureSnapshotManager",
            'KPHYSICAL': "kPhysical",
            'KPHYSICALFILES': "kPhysicalFiles",
            'KGPFS': "kGPFS",
            'KELASTIFILE': "kElastifile",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KISILON': "kIsilon",
            'KFLASHBLADE': "kFlashBlade",
            'KPURE': "kPure",
            'KIBMFLASHSYSTEM': "kIbmFlashSystem",
            'KSQL': "kSQL",
            'KEXCHANGE': "kExchange",
            'KAD': "kAD",
            'KORACLE': "kOracle",
            'KVIEW': "kView",
            'KREMOTEADAPTER': "kRemoteAdapter",
            'KO365': "kO365",
            'KO365PUBLICFOLDERS': "kO365PublicFolders",
            'KO365TEAMS': "kO365Teams",
            'KO365GROUP': "kO365Group",
            'KO365EXCHANGE': "kO365Exchange",
            'KO365ONEDRIVE': "kO365OneDrive",
            'KO365SHAREPOINT': "kO365Sharepoint",
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
        ('snapshot_backend_types',): {
            'None': None,
            'KAWSNATIVE': "kAWSNative",
            'KAWSSNAPSHOTMANAGER': "kAWSSnapshotManager",
            'KPHYSICAL': "kPhysical",
            'KSQL': "kSQL",
            'KORACLE': "kOracle",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KAWSS3': "kAwsS3",
            'KAWSRDSPOSTGRESBACKUP': "kAwsRDSPostgresBackup",
            'KAZURENATIVE': "kAzureNative",
            'KAZURESNAPSHOTMANAGER': "kAzureSnapshotManager",
            'KAZURESQL': "kAzureSQL",
        },
    }

    validations = {
        ('snapshot_backend_types',): {
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
            'action': (str,),  # noqa: E501
            'object_action_key': (str, none_type,),  # noqa: E501
            'pause_params': (ProtectedObjectPauseActionParams,),  # noqa: E501
            'resume_params': (ProtectedObjectResumeActionParams,),  # noqa: E501
            'run_now_params': (ProtectedObjectRunNowActionParams,),  # noqa: E501
            'snapshot_backend_types': ([str], none_type,),  # noqa: E501
            'un_protect_params': (ProtectedObjectUnProtectActionParams,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'action': 'action',  # noqa: E501
        'object_action_key': 'objectActionKey',  # noqa: E501
        'pause_params': 'pauseParams',  # noqa: E501
        'resume_params': 'resumeParams',  # noqa: E501
        'run_now_params': 'runNowParams',  # noqa: E501
        'snapshot_backend_types': 'snapshotBackendTypes',  # noqa: E501
        'un_protect_params': 'unProtectParams',  # noqa: E501
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
    def __init__(self, action, *args, **kwargs):  # noqa: E501
        """ProtectdObjectsActionRequest - a model defined in OpenAPI

        Args:
            action (str): Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params.

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

            object_action_key (str, none_type): Specifies the object action key for any action on the given object.. [optional]  # noqa: E501
            pause_params (ProtectedObjectPauseActionParams): [optional]  # noqa: E501
            resume_params (ProtectedObjectResumeActionParams): [optional]  # noqa: E501
            run_now_params (ProtectedObjectRunNowActionParams): [optional]  # noqa: E501
            snapshot_backend_types ([str], none_type): Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types.. [optional]  # noqa: E501
            un_protect_params (ProtectedObjectUnProtectActionParams): [optional]  # noqa: E501
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


        self.action = action
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)


