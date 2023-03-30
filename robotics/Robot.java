// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.


package frc.robot;

import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import com.revrobotics.*;
import com.revrobotics.CANSparkMaxLowLevel.MotorType;

/**
 * The VM is configured to automatically run this class, and to call the functions corresponding to
 * each mode, as described in the TimedRobot documentation. If you change the name of this class or
 * the package after creating this project, you must also update the build.gradle file in the
 * project.
 */
public class Robot extends TimedRobot {
  private static final String kDefaultAuto = "Default";
  private static final String kCustomAuto = "My Auto";
  private String m_autoSelected;
  private final SendableChooser<String> m_chooser = new SendableChooser<>();

  /**
   * This function is run when the robot is first started up and should be used for any
   * initialization code.
   */
  @Override
  public void robotInit() {
    m_chooser.setDefaultOption("Default Auto", kDefaultAuto);
    m_chooser.addOption("My Auto", kCustomAuto);
    SmartDashboard.putData("Auto choices", m_chooser);
  }

  /**
   * This function is called every robot packet, no matter the mode. Use this for items like
   * diagnostics that you want ran during disabled, autonomous, teleoperated and test.
   *
   * <p>This runs after the mode specific periodic functions, but before LiveWindow and
   * SmartDashboard integrated updating.
   */
  @Override
  public void robotPeriodic() {}

  /**
   * This autonomous (along with the chooser code above) shows how to select between different
   * autonomous modes using the dashboard. The sendable chooser code works with the Java
   * SmartDashboard. If you prefer the LabVIEW Dashboard, remove all of the chooser code and
   * uncomment the getString line to get the auto name from the text box below the Gyro
   *
   * <p>You can add additional auto modes by adding additional comparisons to the switch structure
   * below with additional strings. If using the SendableChooser make sure to add them to the
   * chooser code above as well.
   */
  @Override
  public void autonomousInit() {
    m_autoSelected = m_chooser.getSelected();
    // m_autoSelected = SmartDashboard.getString("Auto Selector", kDefaultAuto);
    System.out.println("Auto selected: " + m_autoSelected);
  }

  /** This function is called periodically during autonomous. */
  @Override
  public void autonomousPeriodic() {
    switch (m_autoSelected) {
      case kCustomAuto:
        // Put custom auto code here
        break;
      case kDefaultAuto:
      default:
        // Put default auto code here
        break;
    }
  }

  /** This function is called once when teleop is enabled. */
  @Override
  public void teleopInit() {}

  /** This function is called periodically during operator control. */
  @Override
  public void teleopPeriodic() {}

  /** This function is called once when the robot is disabled. */
  @Override
  public void disabledInit() {}

  /** This function is called periodically when disabled. */
  @Override
  public void disabledPeriodic() {}

  /** This function is called once when test mode is enabled. */
  @Override
  public void testInit() {

    /* Intilizies both motors and assigns them to a variable */
    public CANSparkMax m_leftMotor = new CANSparkMax(1, MotorType.kBrushless);
    public CANSparkMax m_rightMotor = new CANSparkMax(2, MotorType.kBrushless); 

    /* Intiliazies the encoders and sets them to the proper motor */
    public CANEncoder e_leftMotorEnc = m_rightMotor.getEncoder();
    public CANEncoder e_rightMotorEnc = m_rightMotor.getEncoder();

    /* Degree needed to turn (haven't tested so I don't know yet) */
    int turnLeft = 0;
    int turnRight = 0;

    /* Reset encoder count so I can adjust turning */
    e_leftMotorEnc.setPosition(0);
    e_rightMotorEnc.setPosition(0);

    /* Calls movement function to move the robot out of starting position, function is defined below in moveMotor */
    moveMotor();

    /* First turn, left */
    m_rightMotor.set(turnRight);
    
    /* Calls function to move two feet after turn, uses for loop to do it twice */
    for (int x = 0; x < 2; x++){
      moveMotor();      
    }

    /* Second turn, right */
    m_leftMotor.set(turnLeft);

    /* Calls function to move five feet along the course */
    for (int x = 0; x < 5; x++){
      moveMotor();
    }

    /* Third turn, down */
    m_leftMotor.set(turnLeft);

    /* Calls function to move down in straight line */
    for (int x = 0; x < 2; x++){      
      moveMotor();
    }

    /* Fourth turn, left */
    m_rightMotor.set(turnRight);

    /* Calls function to move staright left */
    moveMotor();

    /* Fifth turn, left */
    m_rightMotor.set(turnRight);

    /* Moves straight up along the course for two feet */
    for (int x = 0; x < 2; x++){
      moveMotor();
    }

    /* Sixith turn, right */
    m_rightMotor.set(turnRight);

    /* Moves straight for a foot */
    moveMotor();

    /* Seventh turn, right & down */
    m_rightMotor.set(turnRight);

    /* Calls function to move straight down for two foot */
    for (int x = 0; x < 2; x++){
      moveMotor();
    }

    /* Eigth turn, right */
    m_leftMotor.set(turnRight);

    /* Calls function to move straight for five feet */
    for (int x = 0; x < 5; x++){
      moveMotor();
    }

    /* Ninth turn, right */
    m_rightMotor.set(turnRight);

    /* Calls function to move up staright for a foot */
    for (int x = 0; x < 2; x++){
      moveMotor();
    }

    /* Tenth turn left */
    m_leftMotor.set(turnLeft);

    /* Final call, moves the robot straight for two feet into the final location */
    for (int x = 0; x < 2; x++){
      moveMotor();
    }
    /* Program and course has finished, clean everything up */
    m_rightMotor.stopMotor();
    m_leftMotor.stopMotor();
    
  }

  /* Function to move the motor for 1 foot */
  public void moveMotor() {

    /* Intilizies both motors and assigns them to a variable */
    public CANSparkMax m_leftMotor = new CANSparkMax(1, MotorType.kBrushless);
    public CANSparkMax m_rightMotor = new CANSparkMax(2, MotorType.kBrushless); 

    /* Intiliazies the encoders and sets them to the proper motor */
    public CANEncoder e_leftMotorEnc = m_rightMotor.getEncoder();
    public CANEncoder e_rightMotorEnc = m_rightMotor.getEncoder();

    /* Proper power to run the motor at to be straight (don't know yet) */
    int strtPowerLeft = 0;
    int strtPowerRight = 0;

    /* Resets the encoder count so I can manipulate it */
    e_leftMotorEnc.setPosition(0);
    e_rightMotorEnc.setPosition(0);

    /* Makes sure the motor moves a whole foot before stopping (leftMotor) */
    if (e_leftMotorEnc.getPosition() < 5280){
      m_leftMotor.set(strtPowerLeft);
    } else {
      m_leftMotor.stopMotor();
    }
    /* Makes sure the motor moves a whole foot before stopping (rightMotor) */
    if (e_rightMotorEnc.getPosition() < 5280){
      m_rightMotor.set(strtPowerRight);
    }else{
      m_rightMotor.stopMotor();
    }

    /* Reset encoder count so I can adjust turning */
    e_leftMotorEnc.setPosition(0);
    e_rightMotorEnc.setPosition(0);

  }

  /** This function is called periodically during test mode. */
  @Override
  public void testPeriodic() {}

}
