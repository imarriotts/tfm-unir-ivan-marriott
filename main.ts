import { Instance } from "@cdktf/provider-aws/lib/instance";
import { AwsProvider } from "@cdktf/provider-aws/lib/provider";
import { App, TerraformOutput, TerraformStack } from "cdktf";
import { Construct } from "constructs";

class MyStack extends TerraformStack {
  // Constants
  private readonly REGION = "us-east-2";
  private readonly INSTANCE_TYPE_MEDIUM = "t2.medium";
  private readonly INSTANCE_TYPE_SMALL = "t2.small";
  private readonly KEY_NAME = "Kafka-Ivan";
  private readonly AMI_SERVER = "ami-017cee7f38edf0750";
  private readonly AMI_WEB_TOOLS = "ami-05fb0b8c1424f266b";
  private readonly SG_GROUP1 = "sg-056d5ec36f1430d39";
  private readonly SG_GROUP2 = "sg-0bca0825627787d30";
  private readonly SUBNET1 = "subnet-0134366d74bcf6fc6";
  private readonly SUBNET2 = "subnet-031e0f7e64de35faa";
  private readonly PROJECT_NAME = "TFM-UNIR";

  constructor(scope: Construct, id: string) {
    super(scope, id);

    new AwsProvider(this, "AWS", {
      region: this.REGION,
    });

    // Instance 1 (Server 2) Configuration
    const instance1 = new Instance(this, "Instance1", {
      ami: this.AMI_SERVER,
      instanceType: this.INSTANCE_TYPE_MEDIUM,
      keyName: this.KEY_NAME,
      subnetId: this.SUBNET1,
      vpcSecurityGroupIds: [this.SG_GROUP1],
      associatePublicIpAddress: true,
      tags: {
        Name: "Server 2",
        Proyecto: this.PROJECT_NAME
      }
    });

    // Instance 2 (Server 3) Configuration
    const instance2 = new Instance(this, "Instance2", {
      ami: this.AMI_SERVER,
      instanceType: this.INSTANCE_TYPE_MEDIUM,
      keyName: this.KEY_NAME,
      subnetId: this.SUBNET2,
      vpcSecurityGroupIds: [this.SG_GROUP1],
      associatePublicIpAddress: true,
      tags: {
        Name: "Server 3",
        Proyecto: this.PROJECT_NAME
      }
    });

    // Instance 3 (Web Tools) Configuration
    const instance3 = new Instance(this, "Instance3", {
      ami: this.AMI_WEB_TOOLS,
      instanceType: this.INSTANCE_TYPE_SMALL,
      keyName: this.KEY_NAME,
      subnetId: this.SUBNET1,
      vpcSecurityGroupIds: [this.SG_GROUP2],
      associatePublicIpAddress: true,
      tags: {
        Name: "Web Tools",
        Proyecto: this.PROJECT_NAME
      }
    });

    // Outputs
    new TerraformOutput(this, "ip_instance1", {
      value: instance1.publicIp,
    });
    new TerraformOutput(this, "ip_instance2", {
      value: instance2.publicIp,
    });
    new TerraformOutput(this, "ip_instance3", {
      value: instance3.publicIp,
    });
  }
}

const app = new App();
new MyStack(app, "kafka-enviroment");
app.synth();
