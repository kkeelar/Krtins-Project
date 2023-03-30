//region_Copyright

/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

//endregion

package frc.robot;

import java.sql.Time;

//navx imports
import com.kauailabs.navx.frc.*;
//spark max/neos imports
import com.revrobotics.*;
import com.revrobotics.CANSparkMaxLowLevel.MotorType;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.Compressor;

//region_Imports

//regular imports
import edu.wpi.first.wpilibj.Counter;
import edu.wpi.first.wpilibj.DigitalInput;
import edu.wpi.first.wpilibj.DoubleSolenoid;
import edu.wpi.first.wpilibj.DriverStation;
import edu.wpi.first.wpilibj.GenericHID.Hand;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.SPI;
import edu.wpi.first.wpilibj.Solenoid;
import edu.wpi.first.wpilibj.SpeedControllerGroup;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;




public void feederFunction(){


    /* Intilizing the different motors and joysticks */
    public CANSparkMax m_Left1 = new CANSparkMax(42, MotorType.kBrushless); //OG 12 
    public CANSparkMax m_Left2 = new CANSparkMax(60, MotorType.kBrushless); //OG 13
    public CANSparkMax m_Right1 = new CANSparkMax(61, MotorType.kBrushless); //OG 1
    public CANSparkMax m_Right2 = new CANSparkMax(62, MotorType.kBrushless); //OG 2

    public Joystick j_Left = new Joystick(0);
    public Joystick j_Right = new Joystick(1);
    public Joystick j_Operator = new Joystick(2);
    public XboxController j_XboxController = new XboxController(4);

    /* I dont know the power needed to go straight */
    int strtPowerLeft = 0;

    if (j_Right.getTrigger()){
        m_left1.set(strtPowerLeft);
        
    }else{
        break;
    }
    
    if (j_right.getTrigger()){
        m_left1.stopMotor();
    }



    /* Intalizing motor and encoder for the feeder */
    public CANSparkMax m_Feeder = new CANSparkMax(4, MotorType.kBrushless); //positive power for in, negative power for out //OG 7
    public CANEncoder e_Feeder = m_Feeder.getEncoder(); //positive when intaking


    /* Power needed to move the ball up to the shooter (Don't know how much it is yet) */
    int fPower = 0;

    /* Resets encoder count to manipulate it */
    e_feeder.setPosition(0);

    /* Moves feeder however much it needs to get the ball into the posistion */
    e_Feeder.setPosition(fPower);

}