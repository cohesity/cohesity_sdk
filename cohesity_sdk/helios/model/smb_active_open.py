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


class SmbActiveOpen(ModelNormal):
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
        ("access_info_list",): {
            "None": None,
            "FILEREADDATA": "FileReadData",
            "FILEWRITEDATA": "FileWriteData",
            "FILEAPPENDDATA": "FileAppendData",
            "FILEREADEA": "FileReadEa",
            "FILEWRITEEA": "FileWriteEa",
            "FILEEXECUTE": "FileExecute",
            "FILEDELETECHILD": "FileDeleteChild",
            "FILEREADATTRIBUTES": "FileReadAttributes",
            "FILEWRITEATTRIBUTES": "FileWriteAttributes",
            "DELETE": "Delete",
            "READCONTROL": "ReadControl",
            "WRITEDAC": "WriteDac",
            "WRITEOWNER": "WriteOwner",
            "SYNCHRONIZE": "Synchronize",
            "ACCESSSYSTEMSECURITY": "AccessSystemSecurity",
            "MAXIMUMALLOWED": "MaximumAllowed",
            "GENERICALL": "GenericAll",
            "GENERICEXECUTE": "GenericExecute",
            "GENERICWRITE": "GenericWrite",
            "GENERICREAD": "GenericRead",
        },
        ("access_privilege",): {
            "None": None,
            "READ": "Read",
            "WRITE": "Write",
            "DELETE": "Delete",
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
        return {
            "open_id": (
                int,
                none_type,
            ),  # noqa: E501
            "access_info_list": (
                [str],
                none_type,
            ),  # noqa: E501
            "access_privilege": (
                [str],
                none_type,
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "open_id": "openId",  # noqa: E501
        "access_info_list": "accessInfoList",  # noqa: E501
        "access_privilege": "accessPrivilege",  # noqa: E501
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
        """SmbActiveOpen - a model defined in OpenAPI

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

            open_id (int, none_type): Specifies the id of the active open.. [optional]  # noqa: E501
            access_info_list ([str], none_type): Specifies the File Access Type. Following documentation was taken from MSDN. https://msdn.microsoft.com/en-us/library/Cc246802.aspx  'FileReadData' indicates the right to read data from the file or named   pipe. 'FileWriteData' indicates the right to write data into the file or named   pipe beyond the end of the file. 'FileAppendData' indicates the right to append data into the file or named   pipe. 'FileReadEa' indicates the right to read the extended attributes of the   file or named pipe. 'FileWriteEa' indicates the right to write or change the extended   attributes to the file or named pipe. 'FileExecute' indicates the right to delete entries within a directory. 'FileDeleteChild' indicates the right to execute the file. 'FileReadAttributes' indicates the right to read the attributes of the   file. 'FileWriteAttributes' indicates the right to change the attributes of the   file. 'Delete' indicates the right to delete the file. 'ReadControl' indicates the right to read the security descriptor for the   file or named pipe. 'WriteDac' indicates the right to change the discretionary access control   list (DACL) in the security descriptor for the file or named pipe. For   the DACL data structure, see ACL in [MS-DTYP]. 'WriteOwner' indicates the right to change the owner in the security   descriptor for the file or named pipe. 'Synchronize' is used only by SMB2 clients. 'AccessSystemSecurity' indicates the right to read or change the system   access control list (SACL) in the security descriptor for the file or   named pipe. For the SACL data structure, see ACL in [MS-DTYP].<42> 'MaximumAllowed' indicates that the client is requesting an open to the   file with the highest level of access the client has on this file.   If no access is granted for the client on this file, the server MUST   fail the open with STATUS_ACCESS_DENIED. 'GenericAll' indicates a request for all the access flags that are   previously listed except MaximumAllowed and AccessSystemSecurity. 'GenericExecute' indicates a request for the following combination of   access flags listed above:   FileReadAttributes| FileExecute| Synchronize| ReadControl. 'GenericWrite' indicates a request for the following combination of   access flags listed above:   FileWriteData| FileAppendData| FileWriteAttributes| FileWriteEa|   Synchronize| ReadControl. 'GenericRead' indicates a request for the following combination of   access flags listed above:   FileReadData| FileReadAttributes| FileReadEa| Synchronize|   ReadControl.. [optional]  # noqa: E501
            access_privilege ([str], none_type): Specifies whether access privilege of others if they're allowed to read/write/delete.. [optional]  # noqa: E501
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
