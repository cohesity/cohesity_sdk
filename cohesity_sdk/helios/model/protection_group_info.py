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
    from cohesity_sdk.helios.model.protection_group_run import ProtectionGroupRun
    globals()['ProtectionGroupRun'] = ProtectionGroupRun


class ProtectionGroupInfo(ModelNormal):
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
            'KVMWARE': "kVMware",
            'KHYPERV': "kHyperV",
            'KSQL': "kSQL",
            'KVIEW': "kView",
            'KREMOTEADAPTER': "kRemoteAdapter",
            'KPHYSICAL': "kPhysical",
            'KPURE': "kPure",
            'KAZURE': "kAzure",
            'KNETAPP': "kNetapp",
            'KGENERICNAS': "kGenericNas",
            'KACROPOLIS': "kAcropolis",
            'KISILON': "kIsilon",
            'KKVM': "kKVM",
            'KAWS': "kAWS",
            'KAWSNATIVE': "kAWSNative",
            'KAWSSNAPSHOTMANAGER': "kAWSSnapshotManager",
            'KRDSSNAPSHOTMANAGER': "kRDSSnapshotManager",
            'KAURORASNAPSHOTMANAGER': "kAuroraSnapshotManager",
            'KEXCHANGE': "kExchange",
            'KORACLE': "kOracle",
            'KGCP': "kGCP",
            'KFLASHBLADE': "kFlashBlade",
            'KO365': "kO365",
            'KHYPERFLEX': "kHyperFlex",
            'KAD': "kAD",
            'KGPFS': "kGPFS",
            'KKUBERNETES': "kKubernetes",
            'KNIMBLE': "kNimble",
            'KELASTIFILE': "kElastifile",
            'KCASSANDRA': "kCassandra",
            'KMONGODB': "kMongoDB",
            'KCOUCHBASE': "kCouchbase",
            'KHDFS': "kHdfs",
            'KHIVE': "kHive",
            'KHBASE': "kHBase",
            'KUDA': "kUDA",
            'KO365SHAREPOINT': "kO365Sharepoint",
            'KO365PUBLICFOLDERS': "kO365PublicFolders",
            'KO365TEAMS': "kO365Teams",
            'KO365GROUP': "kO365Group",
            'KO365EXCHANGE': "kO365Exchange",
            'KO365ONEDRIVE': "kO365OneDrive",
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
            'group_id': (int, none_type,),  # noqa: E501
            'protection_group_id': (str, none_type,),  # noqa: E501
            'group_name': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'last_run': (ProtectionGroupRun,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'group_id': 'groupId',  # noqa: E501
        'protection_group_id': 'protectionGroupId',  # noqa: E501
        'group_name': 'groupName',  # noqa: E501
        'type': 'type',  # noqa: E501
        'last_run': 'lastRun',  # noqa: E501
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
        """ProtectionGroupInfo - a model defined in OpenAPI

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

            group_id (int, none_type): This field is deprecated. 'protectionGroupId' should be used instead. Specifies the id of the Protection Group.. [optional]  # noqa: E501
            protection_group_id (str, none_type): Specifies the protection group id.. [optional]  # noqa: E501
            group_name (str, none_type): Specifies the name of the Protection Group.. [optional]  # noqa: E501
            type (str, none_type): Specifies the type of the Protection Group such as View or Puppeteer. 'Puppeteer' refers to a Remote Adapter Group. Supported environment types such as 'View', 'SQL', 'VMware', etc. NOTE: 'Puppeteer' refers to Cohesity's Remote Adapter. 'VMware' indicates the VMware Protection Source environment. 'HyperV' indicates the HyperV Protection Source environment. 'SQL' indicates the SQL Protection Source environment. 'View' indicates the View Protection Source environment. 'Puppeteer' indicates the Cohesity's Remote Adapter. 'Physical' indicates the physical Protection Source environment. 'Pure' indicates the Pure Storage Protection Source environment. 'Nimble' indicates the Nimble Storage Protection Source environment. 'Azure' indicates the Microsoft's Azure Protection Source environment. 'Netapp' indicates the Netapp Protection Source environment. 'Agent' indicates the Agent Protection Source environment. 'GenericNas' indicates the Generic Network Attached Storage Protection Source environment. 'Acropolis' indicates the Acropolis Protection Source environment. 'PhsicalFiles' indicates the Physical Files Protection Source environment. 'Isilon' indicates the Dell EMC's Isilon Protection Source environment. 'GPFS' indicates IBM's GPFS Protection Source environment. 'KVM' indicates the KVM Protection Source environment. 'AWS' indicates the AWS Protection Source environment. 'Exchange' indicates the Exchange Protection Source environment. 'HyperVVSS' indicates the HyperV VSS Protection Source environment. 'Oracle' indicates the Oracle Protection Source environment. 'GCP' indicates the Google Cloud Platform Protection Source environment. 'FlashBlade' indicates the Flash Blade Protection Source environment. 'AWSNative' indicates the AWS Native Protection Source environment. 'O365' indicates the Office 365 Protection Source environment. 'O365Outlook' indicates Office 365 outlook Protection Source environment. 'HyperFlex' indicates the Hyper Flex Protection Source environment. 'GCPNative' indicates the GCP Native Protection Source environment. 'AzureNative' indicates the Azure Native Protection Source environment. 'Kubernetes' indicates a Kubernetes Protection Source environment. 'Elastifile' indicates Elastifile Protection Source environment. 'AD' indicates Active Directory Protection Source environment.. [optional]  # noqa: E501
            last_run (ProtectionGroupRun): [optional]  # noqa: E501
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


