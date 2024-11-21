from troposphere import Tags, Template
from troposphere.secretsmanager import GenerateSecretString, Secret

t = Template()
t.set_version("2010-09-09")

MySecret = t.add_resource(
    Secret(
        "MySecret",
        Name="MySecret",
        Description="This is an autogenerated secret",
        GenerateSecretString=GenerateSecretString(
            SecretStringTemplate='{"username":"test-user"}',
            GenerateStringKey="password",
            PasswordLength=30,
        ),
        Tags=Tags(Appname="AppA"),
    )
)

print(t.to_json())