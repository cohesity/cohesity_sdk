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
    from cohesity_sdk.helios.model.client_stats_in_last_hours import ClientStatsInLastHours
    globals()['ClientStatsInLastHours'] = ClientStatsInLastHours


class ClientStats(ModelNormal):
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
        ('metric',): {
            'None': None,
            'KNUMBYTESREAD': "kNumBytesRead",
            'KNUMBYTESWRITTEN': "kNumBytesWritten",
            'KREADIOS': "kReadIos",
            'KWRITEIOS': "kWriteIos",
            'KREADLATENCYUSECS': "kReadLatencyUsecs",
            'KWRITELATENCYUSECS': "kWriteLatencyUsecs",
            'KNUMREADERRORS': "kNumReadErrors",
            'KNUMWRITEERRORS': "kNumWriteErrors",
            'KNFSV3MNTLATUSECS': "kNFSv3MntLatUsecs",
            'KNFSV3MNTOPS': "kNFSv3MntOps",
            'KNFSV3MNTERR': "kNFSv3MntErr",
            'KNFSV3UMNTLATUSECS': "kNFSv3UmntLatUsecs",
            'KNFSV3UMNTOPS': "kNFSv3UmntOps",
            'KNFSV3UMNTERR': "kNFSv3UmntErr",
            'KNFSV3CREATELATUSECS': "kNFSv3CreateLatUsecs",
            'KNFSV3CREATEOPS': "kNFSv3CreateOps",
            'KNFSV3CREATEERR': "kNFSv3CreateErr",
            'KNFSV3REMOVELATUSECS': "kNFSv3RemoveLatUsecs",
            'KNFSV3REMOVEOPS': "kNFSv3RemoveOps",
            'KNFSV3REMOVEERR': "kNFSv3RemoveErr",
            'KNFSV3MKDIRLATUSECS': "kNFSv3MkdirLatUsecs",
            'KNFSV3MKDIROPS': "kNFSv3MkdirOps",
            'KNFSV3MKDIRERR': "kNFSv3MkdirErr",
            'KNFSV3RMDIRLATUSECS': "kNFSv3RmdirLatUsecs",
            'KNFSV3RMDIROPS': "kNFSv3RmdirOps",
            'KNFSV3RMDIRERR': "kNFSv3RmdirErr",
            'KNFSV3LOOKUPLATUSECS': "kNFSv3LookupLatUsecs",
            'KNFSV3LOOKUPOPS': "kNFSv3LookupOps",
            'KNFSV3LOOKUPERR': "kNFSv3LookupErr",
            'KNFSV3READDIRLATUSECS': "kNFSv3ReaddirLatUsecs",
            'KNFSV3READDIROPS': "kNFSv3ReaddirOps",
            'KNFSV3READDIRERR': "kNFSv3ReaddirErr",
            'KNFSV3READDIRPLUSLATUSECS': "kNFSv3ReaddirplusLatUsecs",
            'KNFSV3READDIRPLUSOPS': "kNFSv3ReaddirplusOps",
            'KNFSV3READDIRPLUSERR': "kNFSv3ReaddirplusErr",
            'KNFSV3SYMLINKLATUSECS': "kNFSv3SymlinkLatUsecs",
            'KNFSV3SYMLINKOPS': "kNFSv3SymlinkOps",
            'KNFSV3SYMLINKERR': "kNFSv3SymlinkErr",
            'KNFSV3RENAMELATUSECS': "kNFSv3RenameLatUsecs",
            'KNFSV3RENAMEOPS': "kNFSv3RenameOps",
            'KNFSV3RENAMEERR': "kNFSv3RenameErr",
            'KSMBSESSIONSETUPLATUSECS': "kSMBSessionSetupLatUsecs",
            'KSMBSESSIONSETUPOPS': "kSMBSessionSetupOps",
            'KSMBSESSIONSETUPERR': "kSMBSessionSetupErr",
            'KSMBLOGOFFLATUSECS': "kSMBLogoffLatUsecs",
            'KSMBLOGOFFOPS': "kSMBLogoffOps",
            'KSMBLOGOFFERR': "kSMBLogoffErr",
            'KSMBTREECONNECTLATUSECS': "kSMBTreeConnectLatUsecs",
            'KSMBTREECONNECTOPS': "kSMBTreeConnectOps",
            'KSMBTREECONNECTERR': "kSMBTreeConnectErr",
            'KSMBTREEDISCONNECTLATUSECS': "kSMBTreeDisconnectLatUsecs",
            'KSMBTREEDISCONNECTOPS': "kSMBTreeDisconnectOps",
            'KSMBTREEDISCONNECTERR': "kSMBTreeDisconnectErr",
            'KSMBOPENLATUSECS': "kSMBOpenLatUsecs",
            'KSMBOPENOPS': "kSMBOpenOps",
            'KSMBOPENERR': "kSMBOpenErr",
            'KSMBCLOSELATUSECS': "kSMBCloseLatUsecs",
            'KSMBCLOSEOPS': "kSMBCloseOps",
            'KSMBCLOSEERR': "kSMBCloseErr",
            'KSMBCREATEFILELATUSECS': "kSMBCreateFileLatUsecs",
            'KSMBCREATEFILEOPS': "kSMBCreateFileOps",
            'KSMBCREATEFILEERR': "kSMBCreateFileErr",
            'KSMBDELETEFILELATUSECS': "kSMBDeleteFileLatUsecs",
            'KSMBDELETEFILEOPS': "kSMBDeleteFileOps",
            'KSMBDELETEFILEERR': "kSMBDeleteFileErr",
            'KSMBMKDIRLATUSECS': "kSMBMkdirLatUsecs",
            'KSMBMKDIROPS': "kSMBMkdirOps",
            'KSMBMKDIRERR': "kSMBMkdirErr",
            'KSMBRMDIRLATUSECS': "kSMBRmdirLatUsecs",
            'KSMBRMDIROPS': "kSMBRmdirOps",
            'KSMBRMDIRERR': "kSMBRmdirErr",
            'KSMBREADDIRLATUSECS': "kSMBReaddirLatUsecs",
            'KSMBREADDIROPS': "kSMBReaddirOps",
            'KSMBREADDIRERR': "kSMBReaddirErr",
            'KSMBGETINFOLATUSECS': "kSMBGetInfoLatUsecs",
            'KSMBGETINFOOPS': "kSMBGetInfoOps",
            'KSMBGETINFOERR': "kSMBGetInfoErr",
            'KSMBSETINFOLATUSECS': "kSMBSetInfoLatUsecs",
            'KSMBSETINFOOPS': "kSMBSetInfoOps",
            'KSMBSETINFOERR': "kSMBSetInfoErr",
            'KSMBRENAMELATUSECS': "kSMBRenameLatUsecs",
            'KSMBRENAMEOPS': "kSMBRenameOps",
            'KSMBRENAMEERR': "kSMBRenameErr",
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
            'metric': (str, none_type,),  # noqa: E501
            'value': (int, none_type,),  # noqa: E501
            'value_in_last_hours': ([ClientStatsInLastHours], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'metric': 'metric',  # noqa: E501
        'value': 'value',  # noqa: E501
        'value_in_last_hours': 'valueInLastHours',  # noqa: E501
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
        """ClientStats - a model defined in OpenAPI

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

            metric (str, none_type): Specifies the stats metric.. [optional]  # noqa: E501
            value (int, none_type): Specifies the stats value.. [optional]  # noqa: E501
            value_in_last_hours ([ClientStatsInLastHours], none_type): Specifies the stats value in last hours.. [optional]  # noqa: E501
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


