#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
import sys
import os

# CRBasic Program Generator (GUI).py
# A script to output RWIS programs depending on user input as to what sensors are at a site.

# Author: Cody Oppermann & Alex Blackmer
# GUI Author: Alex Blackmer
# Last run: 08/01/2023

# TO DO:
# Build in check to delete program file if it exists.
# Check CR310. Same program as a CR300?
# Write variable checks (i.e., if temp < - 35 or > 135)
# Finalize CR1000 program
# Finalize CR300 program


class StationGui:
    # Constructor function
    def __init__(self):
        self.path = "./Programs/"
        # create root window
        self.root = Tk()
        # root window title and dimension
        self.root.title("CRBasic Program Generator")
        # Set geometry (widthxheight)
        self.root.geometry('580x320')

        # User Name
        self.username = ""
        self.username_var = StringVar()     # Tkinter specific container for string
        username_l = Label(self.root, text="User Name").grid(row=0, column=0)
        username = Entry(self.root, textvariable=self.username_var).grid(row=0, column=1)

        # Date
        self.date = ""
        self.date_var = StringVar()
        date_l = Label(self.root, text="Date (MMDDYY)").grid(row=1, column=0)
        date = Entry(self.root, textvariable=self.date_var).grid(row=1, column=1)

        # Site Name
        self.site_name = ""
        self.site_name_var = StringVar()
        site_name_l = Label(self.root, text="Site Name").grid(row=2, column=0)
        site_name = Entry(self.root, textvariable=self.site_name_var).grid(row=2, column=1)

        # Logger
        self.logger_type = ""
        self.logger_var = StringVar()
        logger_l = Label(self.root, text="Logger Type").grid(row=3, column=0)
        logger_cb = ttk.Combobox(self.root, textvariable=self.logger_var)
        logger_cb['values'] = ('CR1000X', 'CR1000', 'CR3XX')
        logger_cb.grid(row=3, column=1)

        # Anemometer
        self.wind = ""
        self.wind_var = StringVar()
        wind_l = Label(self.root, text="Anemometer Type").grid(row=4, column=0)
        wind_cb = ttk.Combobox(self.root, textvariable=self.wind_var)
        wind_cb['values'] = ('Regular', 'HD')
        wind_cb.grid(row=4, column=1)

        # Thermometer
        self.temp = ""
        self.temp_var = StringVar()
        temp_l = Label(self.root, text="Thermometer Type").grid(row=5, column=0)
        temp_cb = ttk.Combobox(self.root, textvariable=self.temp_var)
        temp_cb['values'] = ('Legacy/HMP60', 'CS215-in-datalogger', 'CS215-in-CS125', 'HygroVUE5/10')
        temp_cb.grid(row=5, column=1)

        # Road Sensor
        self.RS = ""
        self.RS_var = StringVar()
        RS_l = Label(self.root, text="Road Sensor Type").grid(row=6, column=0)
        RS_cb = ttk.Combobox(self.root, textvariable=self.RS_var)
        RS_cb['values'] = ('Vaisala', 'IceSight', 'None')
        RS_cb.grid(row=6, column=1)

        # Road Sensor Com Type
        self.RS_com = None
        self.RS_com_var = IntVar()
        RS_com_Button = Checkbutton(self.root, text="Radio Coms for Road Sensor? ", variable=self.RS_com_var, onvalue=1,
                                     offvalue=0)
        RS_com_Button.grid(row=6, column=2)

        # Ground Temp
        self.subprobe = ""
        self.subprobe_var = StringVar()
        subprobe_l = Label(self.root, text="Subprobe Type").grid(row=7, column=0)
        subprobe_cb = ttk.Combobox(self.root, textvariable=self.subprobe_var)
        subprobe_cb['values'] = ('107', '108', '109', 'None')
        subprobe_cb.grid(row=7, column=1)

        # Snow Depth
        self.Snow = ""
        self.Snow_var = StringVar()
        Snow_l = Label(self.root, text="Snow Depth Sensor Type").grid(row=8, column=0)
        Snow_cb = ttk.Combobox(self.root, textvariable=self.Snow_var)
        Snow_cb['values'] = ('SnowVue', 'SR50', 'None')
        Snow_cb.grid(row=8, column=1)

        # Snow Depth Constant
        self.Snow_const= "0"
        self.Snow_const_var = StringVar()
        Snow_const_entry = Entry(self.root, textvariable=self.Snow_const_var)
        Snow_const_entry.insert(0,"Snow Depth Constant...")
        # Creates temporary text in entry box
        def temp_text(e):
            Snow_const_entry.delete(0, "end")
        Snow_const_entry.bind("<FocusIn>", temp_text)
        Snow_const_entry.grid(row=8, column=2)

        # MISC
        misc_l = Label(self.root, text="Do the following exist at the station?:").grid(row=9, column=1)

        # CS125
        self.CS125 = None
        self.CS125_var = IntVar()
        CS125_Button = Checkbutton(self.root, text="CS125 Present Weather Sensor", variable=self.CS125_var, onvalue=1, offvalue=0)
        CS125_Button.grid(row=10, column=0)

        # Precip
        self.TE525 = None
        self.TE525_var = IntVar()
        TE525_Button = Checkbutton(self.root, text="TE525 Rain Gauge", variable=self.TE525_var, onvalue=1, offvalue=0)
        TE525_Button.grid(row=10, column=1)

        # Pyro
        self.pyro = None
        self.pyro_var = IntVar()
        pyro_Button = Checkbutton(self.root, text="LI200X Pyranometer", variable=self.pyro_var, onvalue=1, offvalue=0)
        pyro_Button.grid(row=10, column=2)

        # CS655
        self.CS655 = None
        self.CS655_var = IntVar()
        CS655_Button = Checkbutton(self.root, text="CS655 Soil Moisture Probe", variable=self.CS655_var, onvalue=1, offvalue=0)
        CS655_Button.grid(row=11, column=0)

        # CC650
        self.CC640 = None
        self.CC640_var = IntVar()
        CC640_Button = Checkbutton(self.root, text="CC640 Camera", variable=self.CC640_var, onvalue=1, offvalue=0)
        CC640_Button.grid(row=11, column=1)

        # SW12V Light
        self.light = None
        self.SW12V_var = IntVar()
        SW12V_Button = Checkbutton(self.root, text="SW12V Light", variable=self.SW12V_var, onvalue=1, offvalue=0)
        SW12V_Button.grid(row=11, column=2)


        # create a Submit Button and place into the root window
        submit = Button(self.root, text="Submit", fg="Black", bg="Red", command=self.validate)
        submit.grid(row=12, column=1)
        self.status = Label(self.root, text="")
        self.status.grid(row=13, column=1)
        self.program_generated = False

        # Execute Tkinter
        self.root.mainloop()

    #Function to take data from GUI window and pass to CRBasic code generator function. Checks to ensure data validity
    def validate(self):
        # If critical variables are empty then print "empty input"
        if (self.username_var.get() == "" or
                self.date_var.get() == "" or
                self.site_name_var.get() == "" or
                self.logger_var.get() == "" or
                self.wind_var.get() == "" or
                self.temp_var.get() == "" or
                self.RS_var.get() == "" or
                self.Snow_var.get() == "" or
                self.subprobe_var.get() == ""):
            self.status.configure(text="Not enough input")
        # Checks if date is in the correct format
        elif len(self.date_var.get()) != 6:
            self.status.configure(text="Date is not in MMDDYY format")
        else:
            self.username = self.username_var.get()
            self.logger_type = self.logger_var.get()
            self.site_name = self.site_name_var.get()
            self.date = self.date_var.get()
            self.username = self.username_var.get()
            self.temp = self.temp_var.get()
            self.wind = self.wind_var.get()
            self.Snow= self.Snow_var.get()
            self.Snow_const= self.Snow_const_var.get()
            self.subprobe = self.subprobe_var.get()
            self.RS = self.RS_var.get()
            self.RS_com = self.RS_com_var.get()
            self.CS125 = self.CS125_var.get()
            self.TE525 = self.TE525_var.get()
            self.pyro = self.pyro_var.get()
            self.CS655 = self.CS655_var.get()
            self.CC640 = self.CC640_var.get()
            self.light = self.SW12V_var.get()

            if self.Snow_const == "" or self.Snow_const == "Snow Depth Constant...":
                self.Snow_const = "0"

            self.status.configure(text="Generation Complete, Closing")
            self.__generate_program()
            sys.exit()

    # Creates CRBasic program
    def __generate_program(self):
        # Checks if Program folder exists, creates if not
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        month = self.date[0:2]
        day = self.date[2:4]
        year = self.date[4:6]
        # BEGIN WRITING CR1000X PROGRAM---------------------------------------------------------------------
        if self.logger_type == "CR1000X":
            filename = "{0}_{1}_Auto.CR1X".format(self.site_name, self.date)
            CR1X_file = open(self.path + filename, "w")

            # HEADER INFO------------------
            CR1X_file.writelines(
                ["'CR1000X program automatically generated by RWISPrograms.py on ", month, "/", day, "/", year, " for ",
                 self.site_name, " \n"])
            CR1X_file.writelines(["'Generator: ", self.username, " \n"])
            CR1X_file.writelines("\n")
            CR1X_file.writelines("'Instruments included: \n")
            if self.temp == "Legacy/HMP60":
                CR1X_file.writelines("'Legacy thermometer (HMP45, Rotronic, EE181)")
            elif self.temp == "'CS215-in-datalogger":
                CR1X_file.writelines("'CS215-in-datalogger")
            elif self.temp == "'CS215-in-CS125":
                CR1X_file.writelines("'CS215-in-CS125")
            elif self.temp == "HygroVUE5/10":
                CR1X_file.writelines("'HygroVUE")

            if self.wind == "Regular":
                CR1X_file.writelines(", 05103 or Legacy Alpine Anemometer")
            else:
                CR1X_file.writelines(", HD or HD Alpine Anemometer")

            if self.CS125 == 1:
                CR1X_file.writelines(", CS125")
            if self.TE525 == 1:
                CR1X_file.writelines(", TE525")
            if self.pyro == 1:
                CR1X_file.writelines(", LI200X")
            if self.Snow == "SR50":
                CR1X_file.writelines(", SR50")
            if self.Snow == "SnowVue":
                CR1X_file.writelines(", SnowVue")
            if self.subprobe == "107" or self.subprobe == "108" or self.subprobe == "109":
                CR1X_file.writelines([", ", self.subprobe])
            if self.CS655 == 1:
                CR1X_file.writelines(", CS655")

            if self.RS == "Vaisala":
                CR1X_file.writelines(", Vaisala DSC/DST")
            elif self.RS == "IceSight":
                CR1X_file.writelines(", IceSight")

            if self.CC640 == 1:
                CR1X_file.writelines(", CC640")

            if self.light == 1:
                CR1X_file.writelines(", SW12V Light(s)")

            CR1X_file.writelines("\n'Output Data Tables: MesoAtmo, MesoRoad, Daily")
            if self.CS125 == 1:
                CR1X_file.writelines(", PresentWx")
            if self.CS655 == 1:
                CR1X_file.writelines(", SoilMoisture")

            # DECLARE CONSTANTS------------------------
            CR1X_file.writelines("\n\n'Declare Constants:")
            if self.Snow == "SR50" or self.Snow == "SnowVue":
                CR1X_file.writelines(["\nConst Snow_initial_dist_in = ", str(self.Snow_const)])
            CR1X_file.writelines(["\nConst TE525_exist = ", str(self.TE525)])
            CR1X_file.writelines(["\nConst solar_exist = ", str(self.pyro)])

            # DECLARE PUBLIC VARIABLES--------------------------------------
            CR1X_file.writelines("\n\n'Declare Public Variables\n'Main Variables")
            CR1X_file.writelines("\nPublic Batt_volt")
            CR1X_file.writelines("\nPublic Air_Temp_f")
            if self.temp != "CS215-in-datalogger":
                CR1X_file.writelines("\nPublic RH_percent")
            CR1X_file.writelines("\nPublic TdC")
            CR1X_file.writelines("\nPublic TdF")
            CR1X_file.writelines("\nPublic TwC")
            CR1X_file.writelines("\nPublic TwF")
            if self.RS == "IceSight":
                CR1X_file.writelines("\nPublic TwFC")
            CR1X_file.writelines("\nPublic Wind_Dir_deg")
            CR1X_file.writelines("\nPublic Wind_Speed_mph")
            CR1X_file.writelines("\nPublic Two_Min_Wind_Dir_deg")
            CR1X_file.writelines("\nPublic Two_Min_Wind_Speed_mph")
            CR1X_file.writelines("\nPublic Precip As String *3")
            CR1X_file.writelines("\nPublic Precip_Intensity As String *8")
            CR1X_file.writelines("\nPublic Solar_w")
            CR1X_file.writelines("\nPublic Ground_18in_Temp_f")
            CR1X_file.writelines("\nPublic SnowfallRate")
            CR1X_file.writelines("\nPublic Rain")
            CR1X_file.writelines("\nPublic Snow_Depth_in")
            if self.light == 1:
                CR1X_file.writelines("\nPublic Light As String *3")
            if self.temp == "CS215-in-datalogger":
                CR1X_file.writelines("\n\nPublic CS215(2)")
                CR1X_file.writelines("\nAlias CS215(1)=AirTC")
                CR1X_file.writelines("\nAlias CS215(2)=RH_percent")
            if self.temp == "CS215-in-CS125":
                CR1X_file.writelines("\n\nPublic CS215num")
            if self.temp == "HygroVUE5/10":
                CR1X_file.writelines("\n\nPublic TRHData(2)")
                CR1X_file.writelines("\nAlias TRHData(1)=AirTC")
                CR1X_file.writelines("\nAlias TRHData(2)=RH")
            if self.Snow== "SR50":
                CR1X_file.writelines(
                    "\n\n'SR50A Variables\nPublic TCDT\nPublic SR50(2)\nAlias SR50(1) = dist_raw_in\nAlias SR50(2) = SR50Quality")
            if self.Snow== "SnowVue":
                CR1X_file.writelines(
                    "\n\n'SnowVue Variables\nPublic TCDT\nPublic SnowVue(2)\nAlias SnowVue(1) = dist_raw_in\nAlias SnowVue(2) = SnowVueQuality")

            if self.RS == "IceSight":
                CR1X_file.writelines("\n\n'Declare IceSight variables")
                CR1X_file.writelines("\nPublic poll As String,icein As String * 110,identifier As String")
                CR1X_file.writelines("\n'for serial sensors")
                CR1X_file.writelines("\nPublic sericesightnum (16) As String")
                CR1X_file.writelines("\nAlias sericesightnum(1)=extra1")
                CR1X_file.writelines("\nAlias sericesightnum(2)=serice_yValue")
                CR1X_file.writelines("\nAlias sericesightnum(3)=serice_xValue")
                CR1X_file.writelines("\nAlias sericesightnum(4)=serice_YXratio")
                CR1X_file.writelines("\nAlias sericesightnum(5)=serice_airtemp_C")
                CR1X_file.writelines("\nAlias sericesightnum(6)=serice_roadtemp_C")
                CR1X_file.writelines("\nAlias sericesightnum(7)=serice_AvgCondIndex")
                CR1X_file.writelines("\nAlias sericesightnum(8)=serice_CurCondIndex")
                CR1X_file.writelines("\nAlias sericesightnum(9)=serice_AvgCondCode")
                CR1X_file.writelines("\nAlias sericesightnum(10)=serice_CurCondCode")
                CR1X_file.writelines("\nAlias sericesightnum(11)=serice_AvgFricIndex")
                CR1X_file.writelines("\nAlias sericesightnum(12)=serice_CurFricIndex")
                CR1X_file.writelines("\nAlias sericesightnum(13)=serice_AvgFricCode")
                CR1X_file.writelines("\nAlias sericesightnum(14)=serice_CurFricCode")
                CR1X_file.writelines("\nAlias sericesightnum(15)=serice_Lens")
                CR1X_file.writelines("\nAlias sericesightnum(16)=serice_Grip")
                CR1X_file.writelines("\n\n'serial ice sight rs485 sensors")
                CR1X_file.writelines("\nPublic icesightnum (20) As String")
                CR1X_file.writelines("\nAlias icesightnum(1)=ice_identifier")
                CR1X_file.writelines("\nAlias icesightnum(2)=ice_yValue")
                CR1X_file.writelines("\nAlias icesightnum(3)=ice_xValue")
                CR1X_file.writelines("\nAlias icesightnum(4)=ice_YXratio")
                CR1X_file.writelines("\nAlias icesightnum(5)=ice_airtemp_C")
                CR1X_file.writelines("\nAlias icesightnum(6)=ice_roadtemp_C")
                CR1X_file.writelines("\nAlias icesightnum(7)=ice_AvgCondIndex")
                CR1X_file.writelines("\nAlias icesightnum(8)=ice_CurCondIndex")
                CR1X_file.writelines("\nAlias icesightnum(9)=ice_AvgCondCode")
                CR1X_file.writelines("\nAlias icesightnum(10)=ice_CurCondCode")
                CR1X_file.writelines("\nAlias icesightnum(11)=ice_AvgFricIndex")
                CR1X_file.writelines("\nAlias icesightnum(12)=ice_CurFricIndex")
                CR1X_file.writelines("\nAlias icesightnum(13)=ice_AvgFricCode")
                CR1X_file.writelines("\nAlias icesightnum(14)=ice_CurFricCode")
                CR1X_file.writelines("\nAlias icesightnum(15)=ice_Lens")
                CR1X_file.writelines("\nAlias icesightnum(16)=ice_Grip")
                CR1X_file.writelines("\nAlias icesightnum(17)=fill1")
                CR1X_file.writelines("\nAlias icesightnum(18)=fill2")
                CR1X_file.writelines("\nAlias icesightnum(19)=fill3")
                CR1X_file.writelines("\nAlias icesightnum(20)=fill4")
                CR1X_file.writelines("\n\nPublic iceAirTemp_C")
                CR1X_file.writelines("\nPublic iceAirTemp_F")
                CR1X_file.writelines("\nPublic iceRoadTemp_C")
                CR1X_file.writelines("\nPublic iceRoadTemp_F")
            if self.CS655 == 1:
                CR1X_file.writelines(
                    "\n\n'CS655 Variables\nPublic CS655(6)\nAlias CS655(1) = VWC\nAlias CS655(2) = EC\nAlias CS655(3) = T\nAlias CS655(4) = P\nAlias CS655(5) = PA\nAlias CS655(6) = VR")

            # CS125 Variables
            CR1X_file.writelines("\n\n'CS125 Variables")
            CR1X_file.writelines("\nDim CheckVal As Long, TempString As String")
            CR1X_file.writelines("\nDim NBytesReturned, OutString As String * 40")
            CR1X_file.writelines("\nPublic CS125_In As String * 200")
            CR1X_file.writelines("\nPublic cs125out(27) As String")
            CR1X_file.writelines("\nAlias cs125out(1)=messID")
            CR1X_file.writelines("\nAlias cs125out(2)=sensorID")
            CR1X_file.writelines("\nAlias cs125out(3)=sysStatus")
            CR1X_file.writelines("\nAlias cs125out(4)=messInterval")
            CR1X_file.writelines("\nAlias cs125out(5)=vis_m_string")
            CR1X_file.writelines("\nAlias cs125out(6)=visUnits")
            CR1X_file.writelines("\nAlias cs125out(7)=avgDuration")
            CR1X_file.writelines("\nAlias cs125out(8)=userAlarm_1")
            CR1X_file.writelines("\nAlias cs125out(9)=userAlarm_2")
            CR1X_file.writelines("\nAlias cs125out(10)=Emitter_failure")
            CR1X_file.writelines("\nAlias cs125out(11)=Emitter_lens_dirty")
            CR1X_file.writelines("\nAlias cs125out(12)=Emitter_temp_error")
            CR1X_file.writelines("\nAlias cs125out(13)=Detector_lens_dirty")
            CR1X_file.writelines("\nAlias cs125out(14)=Detector_temp_error")
            CR1X_file.writelines("\nAlias cs125out(15)=Detector_saturated")
            CR1X_file.writelines("\nAlias cs125out(16)=Hood_temp_error")
            CR1X_file.writelines("\nAlias cs125out(17)=Ext_temp_error")
            CR1X_file.writelines("\nAlias cs125out(18)=Signature_error")
            CR1X_file.writelines("\nAlias cs125out(19)=Flash_read_error")
            CR1X_file.writelines("\nAlias cs125out(20)=Flash_write_error")
            CR1X_file.writelines("\nAlias cs125out(21)=Particle_limit_error")
            CR1X_file.writelines("\nAlias cs125out(22)=Particle_count")
            CR1X_file.writelines("\nAlias cs125out(23)=Intensity_mm_hr")
            CR1X_file.writelines("\nAlias cs125out(24)=SYNOPCode")
            CR1X_file.writelines("\nAlias cs125out(25)=PresentWeather")
            CR1X_file.writelines("\nAlias cs125out(26)=CS125Temp")
            CR1X_file.writelines("\nAlias cs125out(27)=CS125RH")
            CR1X_file.writelines("\n\nPublic visibility_m\nPublic visibility_mi")

            # DSC/DST Variables
            if self.RS == "Vaisala":
                CR1X_file.writelines(["\n\n'DSC/DST Variables"])
                CR1X_file.writelines(["\nPublic dstinputvolt, dstinputvoltfilter As String"])
                CR1X_file.writelines(["\nPublic dsthardwarestatus, dsthardwarestatusfilter As String"])
                CR1X_file.writelines(["\nPublic dscsurfstatus,dscsurfstatusfilter As String"])
                CR1X_file.writelines(["\nPublic dsclevelofgrip,dsclevelofgripfilter As String"])
                CR1X_file.writelines(["\nPublic dschardwarestatus, dschardwarestatusfilter As String"])
                CR1X_file.writelines(["\nPublic dscamtofwater,dscamtofwaterfilter As String"])
                CR1X_file.writelines(["\nPublic dscamtofice,dscamtoficefilter As String"])
                CR1X_file.writelines(["\nPublic dscamtofsnow,dscamtofsnowfilter As String"])
                CR1X_file.writelines(["\nPublic dstAirTemp_F"])
                CR1X_file.writelines(["\nPublic dstDewPt_F"])
                CR1X_file.writelines(["\nPublic dstRoadTemp_F"])
                CR1X_file.writelines(["\nPublic dscRoadStatus As String"])
                CR1X_file.writelines(["\nPublic dscraw As String * 400"])
                CR1X_file.writelines(["\nPublic dscpoll As String"])
                CR1X_file.writelines(["\nPublic dstairtemp,dstairtempfilter As String"])
                CR1X_file.writelines(["\nPublic dstrh,dstrhfilter As String"])
                CR1X_file.writelines(["\nPublic dstdewpoint,dstdewpointfilter As String"])
                CR1X_file.writelines(["\nPublic dstsurfacetemp,dstsurfacetempfilter As String"])
                CR1X_file.writelines(["\nPublic dsccheck"])


            # DECLARE PRIVATE VARIABLES---------------------------------------------------------
            CR1X_file.writelines(["\n\n'Declare Private Variables"])
            CR1X_file.writelines(["\nDim AirTC_9"])
            CR1X_file.writelines(["\nDim SPkPa_6"])
            CR1X_file.writelines(["\nDim Twg_7"])
            CR1X_file.writelines(["\nDim Twpg_8"])
            CR1X_file.writelines(["\nDim Vpg_9"])
            CR1X_file.writelines(["\nDim Vp_10"])
            CR1X_file.writelines(["\nDim SVp_11"])
            CR1X_file.writelines(["\nDim Twch_12"])
            CR1X_file.writelines(["\nDim VpgVpd_13"])
            CR1X_file.writelines(["\nDim Top_14"])
            CR1X_file.writelines(["\nDim Bottom_15"])
            CR1X_file.writelines(["\nDim N_17"])

            # DEFINE UNITS-----------------------
            CR1X_file.writelines("\n\n'Define Units")
            CR1X_file.writelines("\nUnits Air_Temp_f=Deg F")
            CR1X_file.writelines("\nUnits RH_percent=%")
            CR1X_file.writelines("\nUnits Wind_Speed_mph=miles/hour")
            CR1X_file.writelines("\nUnits Wind_Dir_deg=Degrees")
            CR1X_file.writelines("\nUnits Snow_Depth_in=inches")
            CR1X_file.writelines("\nUnits Solar_w=W/m\u00b22")
            CR1X_file.writelines("\nUnits Batt_volt=Volts")
            CR1X_file.writelines("\nUnits visibility_mi=miles")
            CR1X_file.writelines("\nUnits TdF=Deg F")
            CR1X_file.writelines("\nUnits TwF=Deg F")
            CR1X_file.writelines("\nUnits SnowfallRate=in/hr")
            CR1X_file.writelines("\nUnits Rain=inches")
            CR1X_file.writelines("\nUnits Ground_18in_Temp_f=Deg F")
            if self.RS == "Vaisala":
                CR1X_file.writelines("\nUnits dstAirTemp_F=Deg F")
                CR1X_file.writelines("\nUnits dstrh=%")
                CR1X_file.writelines("\nUnits dstDewPt_F=Deg F")
                CR1X_file.writelines("\nUnits dstinputvolt=Volts")
                CR1X_file.writelines("\nUnits dstRoadTemp_F=Deg F")
            if self.RS == "IceSight":
                CR1X_file.writelines("\nUnits iceAirTemp_F=Deg F")
                CR1X_file.writelines("\nUnits iceRoadTemp_F=Deg F")
            if self.CS655 == 1:
                CR1X_file.writelines("\nUnits VWC=m^3/m^3")
                CR1X_file.writelines("\nUnits EC=dS/m")
                CR1X_file.writelines("\nUnits T=Deg F")
                CR1X_file.writelines("\nUnits PA=nSec")
            # dscamt variable units?

            # DEFINE DATA TABLES---------------------------------
            # MesoAtmo Table
            CR1X_file.writelines("\n\n'Define Data Tables")
            CR1X_file.writelines("\n'MesoAtmo table")
            CR1X_file.writelines("\nDataTable (MesoAtmo,1,1008)")
            CR1X_file.writelines("\n  DataInterval (0,10,min,10)")
            CR1X_file.writelines("\n  Sample (1,Air_Temp_f,FP2)")
            CR1X_file.writelines("\n  Sample (1,RH_percent,FP2)")
            CR1X_file.writelines("\n  Sample (1,Two_Min_Wind_Dir_deg,FP2)")
            CR1X_file.writelines("\n  Sample (1,Two_Min_Wind_Speed_mph,FP2)")
            CR1X_file.writelines("\n  Maximum (1,Wind_Speed_mph,FP2,False,True)")
            CR1X_file.writelines("\n  Sample (1,Precip,String)")
            CR1X_file.writelines("\n  Sample (1,Precip_Intensity,String)")
            CR1X_file.writelines("\n  Average (1,Snow_Depth_in,FP2,False)")
            CR1X_file.writelines("\n  Average (1,Solar_w,FP2,False)")
            CR1X_file.writelines("\n  Sample (1,Batt_volt,FP2)")
            CR1X_file.writelines("\n  Sample (1,visibility_mi,FP2)")
            CR1X_file.writelines("\n  Sample (1,TdF,FP2)")
            CR1X_file.writelines("\n  Sample (1,TwF,FP2)")
            CR1X_file.writelines("\n  Sample (1,SnowfallRate,FP2)")
            CR1X_file.writelines("\n  Totalize (1,Rain,FP2,False)")
            CR1X_file.writelines("\nEndTable")
            # MesoRoad Table
            CR1X_file.writelines("\n\n'MesoRoad table")
            CR1X_file.writelines("\nDataTable (MesoRoad,1,1008)")
            CR1X_file.writelines("\n  DataInterval (0,10,min,10)")
            CR1X_file.writelines("\n  Sample (1,Ground_18in_Temp_f,FP2)")
            if self.RS == "Vaisala":
                CR1X_file.writelines("\n  Sample (1,dstAirTemp_F,FP2)")
                CR1X_file.writelines("\n  Sample (1,dstrh,FP2)")
                CR1X_file.writelines("\n  Sample (1,dstDewPt_F,FP2)")
                CR1X_file.writelines("\n  Sample (1,dstinputvolt,FP2)")
                CR1X_file.writelines("\n  Sample (1,dstRoadTemp_F,FP2)")
                CR1X_file.writelines("\n  Sample (1,dsthardwarestatus,FP2)")
                CR1X_file.writelines("\n  Sample (1,dscsurfstatus,FP2)")
                CR1X_file.writelines("\n  Sample (1,dscRoadStatus,String)")
                CR1X_file.writelines("\n  Sample (1,dsclevelofgrip,FP2)")
                CR1X_file.writelines("\n  Sample (1,dschardwarestatus,FP2)")
                CR1X_file.writelines("\n  Sample (1,dscamtofwater,FP2)")
                CR1X_file.writelines("\n  Sample (1,dscamtofice,FP2)")
                CR1X_file.writelines("\n  Sample (1,dscamtofsnow,FP2)")
            if self.RS == "IceSight":
                CR1X_file.writelines("\n  Sample (1,ice_yValue,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_xValue,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_YXratio,FP2")
                CR1X_file.writelines("\n  Sample (1,iceAirTemp_F,FP2)")
                CR1X_file.writelines("\n  Sample (1,iceRoadTemp_F,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_AvgCondIndex,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_CurCondIndex,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_AvgCondCode,String)")
                CR1X_file.writelines("\n  Sample (1,ice_CurCondCode,String)")
                CR1X_file.writelines("\n  Sample (1,ice_AvgFricIndex,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_CurFricIndex,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_AvgFricCode,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_CurFricCode,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_Lens,FP2)")
                CR1X_file.writelines("\n  Sample (1,ice_Grip,String)")
            CR1X_file.writelines("\nEndTable")
            # Daily Table
            CR1X_file.writelines("\n\n'Daily table")
            CR1X_file.writelines("\nDataTable (Daily,1,-1)")
            CR1X_file.writelines("\n  DataInterval (0,1440,min,10)")
            CR1X_file.writelines("\n  Minimum (1,Batt_Volt,FP2,False,True)")
            CR1X_file.writelines("\n  Maximum (1,Air_Temp_f,FP2,False,True)")
            CR1X_file.writelines("\n  Minimum (1,Air_Temp_f,FP2,False,True)")
            CR1X_file.writelines("\n  Maximum (1,RH_percent,FP2,False,True)")
            CR1X_file.writelines("\n  Minimum (1,RH_percent,FP2,False,True)")
            CR1X_file.writelines("\n  Maximum (1,TdF,FP2,False,True)")
            CR1X_file.writelines("\n  Minimum (1,TdF,FP2,False,True)")
            CR1X_file.writelines("\n  Maximum (1,TwF,FP2,False,True)")
            CR1X_file.writelines("\n  Minimum (1,TwF,FP2,False,True)")
            CR1X_file.writelines("\n  Average (1,Wind_Speed_mph,FP2,False)")
            CR1X_file.writelines("\n  Maximum (1,Wind_Speed_mph,FP2,False,True)")
            CR1X_file.writelines("\n  Average (1,Ground_18in_Temp_f,FP2,False)")
            CR1X_file.writelines("\n  Totalize (1,Solar_w,IEEE4,False)")
            CR1X_file.writelines("\nEndTable")
            # PresentWx Table
            if self.CS125 == 1:
                CR1X_file.writelines("\n\n'PresentWx table")
                CR1X_file.writelines("\nDataTable (PresentWx,1,1008)")
                CR1X_file.writelines("\n  DataInterval (0,10,min,10)")
                CR1X_file.writelines("\n  Sample (1,visibility_mi,FP2)")
                CR1X_file.writelines("\n  Sample (1,Particle_count,FP2)")
                CR1X_file.writelines("\n  Sample (1,Intensity_mm_hr,FP2)")
                CR1X_file.writelines("\n  Sample (1,SYNOPCode,FP2)")
                CR1X_file.writelines("\n  Sample (1,PresentWeather,String)")
                CR1X_file.writelines("\n  Sample (1,sysStatus,FP2)")
                CR1X_file.writelines("\n  Sample (1,Emitter_failure,FP2)")
                CR1X_file.writelines("\n  Sample (1,Emitter_lens_dirty,FP2)")
                CR1X_file.writelines("\n  Sample (1,Emitter_temp_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Detector_lens_dirty,FP2)")
                CR1X_file.writelines("\n  Sample (1,Detector_temp_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Detector_saturated,FP2)")
                CR1X_file.writelines("\n  Sample (1,Hood_temp_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Ext_temp_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Signature_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Flash_read_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Flash_write_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,Particle_limit_error,FP2)")
                CR1X_file.writelines("\n  Sample (1,CS125Temp,FP2)")
                CR1X_file.writelines("\n  Sample (1,CS125RH,FP2)")
                CR1X_file.writelines("\nEndTable")
            # SoilMoisture Table
            if self.CS655 == 1:
                CR1X_file.writelines("\n\n'SoilMoisture table")
                CR1X_file.writelines("\nDataTable (SoilMoisture,1,-1)")
                CR1X_file.writelines("\n  DataInterval (0,10,min,10)")
                CR1X_file.writelines("\n  Average (1,VWC,FP2,False)")
                CR1X_file.writelines("\n  Average (1,EC,FP2,False)")
                CR1X_file.writelines("\n  Average (1,T,FP2,False)")
                CR1X_file.writelines("\n  Average (1,P,FP2,False)")
                CR1X_file.writelines("\n  Average (1,PA,FP2,False)")
                CR1X_file.writelines("\n  Average (1,VR,FP2,False)")
                CR1X_file.writelines("\nEndTable")
            # TwoMinute Table
            CR1X_file.writelines("\n\n'TwoMinute table (for wind)")
            CR1X_file.writelines("\nDataTable (TwoMinute,1,-1)")
            CR1X_file.writelines("\n  DataInterval (0,120,sec,10)")
            CR1X_file.writelines("\n  WindVector (1,Wind_Speed_mph,Wind_Dir_deg,FP2,False,0,0,1)")
            CR1X_file.writelines("\nEndTable\n")

            # DEFINE SUBROUTINES (For SR50 and Vaisala DSC/DST)-----------------------------------
            if self.Snow== "SR50" or self.Snow== "SnowVue" or self.RS == "Vaisala" or self.RS == "IceSight":
                CR1X_file.writelines("\n'Define Subroutines")
                if self.Snow== "SR50":
                    # SR50 subroutine
                    CR1X_file.writelines("\nSub SR50A")
                    CR1X_file.writelines(
                        "\n'SR50 Sonic Ranging Sensor (SDI-12 Output) measurements DT, TCDT, & Snow_Depth_in:")
                    CR1X_file.writelines("\n  SDI12Recorder(SR50(),C7,0,\"M6!\",1,0)")
                    CR1X_file.writelines("\n  TCDT=dist_raw_in*SQR((((Air_Temp_f-32)/1.8)+273.15)/273.15)")
                    CR1X_file.writelines("\n  Snow_Depth_in=Snow_initial_dist_in-TCDT")
                    CR1X_file.writelines("\n\n  If Snow_Depth_in = Snow_initial_dist_in Then")
                    CR1X_file.writelines("\n    Snow_Depth_in = \"NAN\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\nEndSub\n")
                if self.Snow== "SnowVue":
                    # SnowVue subroutine
                    CR1X_file.writelines("\nSub SnowVue")
                    CR1X_file.writelines(
                        "\n'SnowVue Sonic Ranging Sensor (SDI-12 Output) measurements DT, TCDT, & Snow_Depth_in:")
                    CR1X_file.writelines("\n  SDI12Recorder(SnowVue(),C7,0,\"M1!\",1,0)")
                    CR1X_file.writelines("\n  dist_raw_in = dist_raw_in*39.3701")
                    CR1X_file.writelines("\n  TCDT=dist_raw_in*SQR((((Air_Temp_f-32)/1.8)+273.15)/273.15)")
                    CR1X_file.writelines("\n  Snow_Depth_in=Snow_initial_dist_in-TCDT")
                    CR1X_file.writelines("\n\n  If Snow_Depth_in = Snow_initial_dist_in Then")
                    CR1X_file.writelines("\n    Snow_Depth_in = \"NAN\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\nEndSub\n")
                if self.RS == "Vaisala":
                    # DSCparse subroutine
                    CR1X_file.writelines("\nSub DSCParse")
                    CR1X_file.writelines("\n'Parse the DSC/DST111 Variables")
                    CR1X_file.writelines("\n  SplitStr (dstairtemp,dscraw,dstairtempfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dstrh,dscraw,dstrhfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dstdewpoint,dscraw,dstdewpointfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dstinputvolt,dscraw,dstinputvoltfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dstsurfacetemp,dscraw,dstsurfacetempfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dsthardwarestatus,dscraw,dsthardwarestatusfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dscsurfstatus,dscraw,dscsurfstatusfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dsclevelofgrip,dscraw,dsclevelofgripfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dschardwarestatus,dscraw,dschardwarestatusfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dscamtofwater,dscraw,dscamtofwaterfilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dscamtofice,dscraw,dscamtoficefilter,1,4)")
                    CR1X_file.writelines("\n  SplitStr (dscamtofsnow,dscraw,dscamtofsnowfilter,1,4)")
                    CR1X_file.writelines("\nEndSub\n")
                    # DSCconvert subroutine
                    CR1X_file.writelines("\nSub DSCconvert")
                    CR1X_file.writelines("\n'Convert the DSC111 and DST111 variables into English units")
                    CR1X_file.writelines("\n  dstAirTemp_F = dstairtemp*1.8+32")
                    CR1X_file.writelines("\n  dstDewPt_F = dstdewpoint*1.8+32")
                    CR1X_file.writelines("\n  dstRoadTemp_F = dstsurfacetemp*1.8+32")
                    CR1X_file.writelines("\n  If dscsurfstatus = 0 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Error\"")
                    CR1X_file.writelines(
                        "\n\n  'When there is a weather alert, the surface code becomes a 3-digit number so")
                    CR1X_file.writelines(
                        "\n  'we need to convert it to a single digit since there is no need for the alert")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 101 OR dscsurfstatus = 201 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 1")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 103 OR dscsurfstatus = 203 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 3")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 105 OR dscsurfstatus = 205 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 5")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 106 OR dscsurfstatus = 206 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 6")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 107 OR dscsurfstatus = 207 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 7")
                    CR1X_file.writelines("\n\n  ElseIf dscsurfstatus = 109 OR dscsurfstatus = 209 Then")
                    CR1X_file.writelines("\n    dscsurfstatus = 9")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  If dscsurfstatus = \"NAN\" Then")
                    CR1X_file.writelines("\n    dscRoadstatus = \"NAN\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 1 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Dry\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 2 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Damp\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 3 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Wet\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 5 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Frost\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 6 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Snow\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 7 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Ice\"")
                    CR1X_file.writelines("\n  ElseIf dscsurfstatus = 9 Then")
                    CR1X_file.writelines("\n    dscRoadStatus = \"Slush\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\nEndSub\n")
                    # DSCOnOff subroutine
                    CR1X_file.writelines("\nSub DSCOnOff")
                    CR1X_file.writelines("\n'Convert variables to NAN if there is no data")
                    CR1X_file.writelines("\n  If dscraw = \"\" Then")
                    CR1X_file.writelines("\n    dscpoll = \"NAN\"")
                    CR1X_file.writelines("\n    dstairtemp = \"NAN\"")
                    CR1X_file.writelines("\n    dstairtempfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dstrh = \"NAN\"")
                    CR1X_file.writelines("\n    dstrhfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dstdewpoint = \"NAN\"")
                    CR1X_file.writelines("\n    dstdewpointfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dstinputvolt = \"NAN\"")
                    CR1X_file.writelines("\n    dstinputvoltfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dstsurfacetemp = \"NAN\"")
                    CR1X_file.writelines("\n    dstsurfacetempfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dsthardwarestatus = \"NAN\"")
                    CR1X_file.writelines("\n    dsthardwarestatusfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dscsurfstatus = \"NAN\"")
                    CR1X_file.writelines("\n    dscsurfstatusfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dsclevelofgrip = \"NAN\"")
                    CR1X_file.writelines("\n    dsclevelofgripfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dschardwarestatus = \"NAN\"")
                    CR1X_file.writelines("\n    dschardwarestatusfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtofwater = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtofwaterfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtofice = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtoficefilter = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtofsnow = \"NAN\"")
                    CR1X_file.writelines("\n    dscamtofsnowfilter = \"NAN\"")
                    CR1X_file.writelines("\n    dstAirTemp_F = \"NAN\"")
                    CR1X_file.writelines("\n    dstDewPt_F = \"NAN\"")
                    CR1X_file.writelines("\n    dstRoadTemp_F = \"NAN\"")
                    CR1X_file.writelines("\n    dscRoadStatus = \"NAN\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\nEndSub\n")
                if self.RS == "IceSight":
                    # parseice485 subroutine
                    CR1X_file.writelines("\nSub parseice485")
                    CR1X_file.writelines("\n  SplitStr (icesightnum(),icein,CHR(32),20,7)")
                    CR1X_file.writelines("\n  iceAirTemp_C = ice_airtemp_C")
                    CR1X_file.writelines("\n  iceAirTemp_F = iceAirTemp_C*1.8+32")
                    CR1X_file.writelines("\n  iceRoadTemp_C = ice_roadtemp_C")
                    CR1X_file.writelines("\n  iceRoadTemp_F = iceRoadTemp_C*1.8+32")
                    CR1X_file.writelines("\n  If ice_AvgFricCode > 1 Then")
                    CR1X_file.writelines("\n    ice_AvgFricCode = \"NAN\"")
                    CR1X_file.writelines("\n    ice_AvgCondCode = \"NAN\"")
                    CR1X_file.writelines("\n  ElseIf ice_AvgFricCode > 0.82")
                    CR1X_file.writelines("\n    ice_AvgFricCode = \"NAN\"")
                    CR1X_file.writelines("\n    ice_AvgCondCode = \"FOG\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\nEndSub\n")

            # MAIN PROGRAM--------------------------
            CR1X_file.writelines("\n'Main Program")
            CR1X_file.writelines("\nBeginProg")

            # 1-Second Section
            CR1X_file.writelines("\nScan (1,Sec,0,0)")
            # Battery Voltage
            CR1X_file.writelines("\n\n  Battery (Batt_volt)")
            # CC640
            if self.CC640 == 1:
                CR1X_file.writelines("\n\n  'CC640")
                CR1X_file.writelines("\n  If TimeIntoInterval (0,10,Min)")
                CR1X_file.writelines("\n    PulsePort (C8,10000)")
                CR1X_file.writelines("\n  EndIf")
            # Anemometer
            if self.wind == "Regular":
                CR1X_file.writelines("\n\n  '(Regular) Wind Speed & Direction Sensor measurements WS_ms and Wind_Dir_Deg:")
                CR1X_file.writelines("\n  PulseCount (Wind_Speed_mph,1,P1,5,1,.2192,0)")
            else:
                CR1X_file.writelines("\n\n  '(HD) Wind Speed & Direction Sensor measurements WS_ms and Wind_Dir_Deg:")
                CR1X_file.writelines("\n  PulseCount (Wind_Speed_mph,1,P1,5,1,.3726,0)")
            CR1X_file.writelines("\n  BrHalf (Wind_Dir_deg,1,mV5000,1,Vx1,1,2500,True,20000,_60Hz,355,0)")
            CR1X_file.writelines("\n  If Wind_Dir_deg>=355 Then Wind_Dir_deg=0")
            CR1X_file.writelines("\n  'Pull two minute values from the two minute table")
            CR1X_file.writelines("\n  Two_Min_Wind_Speed_mph=TwoMinute.Wind_Speed_mph_WVc(1)")
            CR1X_file.writelines("\n  Two_Min_Wind_Dir_deg=TwoMinute.Wind_Speed_mph_WVc(2)")
            # Subprobe
            if self.subprobe == "107":
                CR1X_file.writelines("\n\n  '107 - Sub Temperature Probe measurement 18in_Ground_Temp_F:")
                CR1X_file.writelines("\n  Therm107(Ground_18in_Temp_f,1,2,Vx1,0,_60Hz,1.8,32.0)")
            elif self.subprobe == "108":
                CR1X_file.writelines("\n\n  '108 - Sub Temperature Probe measurement 18in_Ground_Temp_F:")
                CR1X_file.writelines("\n  Therm108(Ground_18in_Temp_f,1,2,Vx1,0,_60Hz,1.8,32.0)")
            elif self.subprobe == "109":
                CR1X_file.writelines("\n\n  '109 - Sub Temperature Probe measurement 18in_Ground_Temp_F:")
                CR1X_file.writelines("\n  Therm109(Ground_18in_Temp_f,1,2,Vx1,0,_60Hz,1.8,32.0)")
            else:
                CR1X_file.writelines("\n\n  'No subprobe:")
                CR1X_file.writelines("\n  Ground_18in_Temp_f = \"NAN\"")
            # Legacy and CS215 Thermometers
            if self.temp == "Legacy/HMP60" or self.temp == "CS215-in-datalogger" or self.temp == "CS215-in-CS125":
                if self.temp == "Legacy/HMP60":
                    CR1X_file.writelines(
                        "\n\n  'Rotronic, EE181, or HMP45C Temp/RH Sensor Measurements Air_Temp_f and RH_Percent:")
                    CR1X_file.writelines("\n  VoltSe (Air_Temp_f,1,mV1000,3,0,0,_60Hz,0.18,-40.0)")
                    CR1X_file.writelines("\n  VoltSe (RH_percent,1,mV1000,4,0,0,_60Hz,0.1,0)")
                if self.temp == "CS215-in-datalogger":
                    CR1X_file.writelines("\n\n  'CS215 (wired into CR1000X) Measurements:")
                    CR1X_file.writelines("\n  SDI12Recorder (CS215(),C1,0,\"M!\",1.0,0)")
                    CR1X_file.writelines("\n  Air_Temp_f = AirTC*1.8 + 32")
                if self.temp == "CS215-in-CS125":
                    CR1X_file.writelines("\n\n  'CS215 (wired into CS125) Measurements:")
                    CR1X_file.writelines("\n  CS215num = CS125Temp")
                    CR1X_file.writelines("\n  Air_Temp_f = (CS215num*1.8)+32")
                    CR1X_file.writelines("\n  RH_percent = CS125RH")
                CR1X_file.writelines("\n  If RH_percent>100 Then RH_percent=100")
                # Dew Point and Wet Bulb Calcs
                CR1X_file.writelines("\n  'Dew Point and Wet-Bulb Calculation Prep")
                CR1X_file.writelines("\n  AirTC_9=(5/9)*(Air_Temp_f-32)")
                CR1X_file.writelines("\n  SPkPa_6=101.325")
                CR1X_file.writelines("\n  SatVP(SVp_11,AirTC_9)")
                CR1X_file.writelines("\n  Vp_10=RH_percent*SVp_11/100")
                CR1X_file.writelines("\n  'Dew Point calculation TdF")
                CR1X_file.writelines("\n  DewPoint(TdC,AirTC_9,RH_percent)")
                CR1X_file.writelines("\n  If TdC>AirTC_9 OR TdC=NAN Then TdC=AirTC_9")
                CR1X_file.writelines("\n  TdF=1.8*TdC+32")
                CR1X_file.writelines("\n  'Find Wet-Bulb TwF")
                CR1X_file.writelines("\n  Top_14=AirTC_9")
                CR1X_file.writelines("\n  Bottom_15=TdC")
                CR1X_file.writelines("\n  For N_17 = 1 To 25")
                CR1X_file.writelines("\n    Twpg_8=Twg_7")
                CR1X_file.writelines("\n    Twg_7=((Top_14-Bottom_15)/2)+Bottom_15")
                CR1X_file.writelines("\n    WetDryBulb(Vpg_9,AirTC_9,Twg_7,SPkPa_6)")
                CR1X_file.writelines("\n    VpgVpd_13=Vpg_9-Vp_10")
                CR1X_file.writelines("\n    Twch_12=ABS(Twpg_8-Twg_7)")
                CR1X_file.writelines("\n    If VpgVpd_13>0 Then")
                CR1X_file.writelines("\n      Top_14=Twg_7")
                CR1X_file.writelines("\n    Else")
                CR1X_file.writelines("\n      Bottom_15=Twg_7")
                CR1X_file.writelines("\n    EndIf")
                CR1X_file.writelines("\n    If Twch_12<0.01 OR N_17=25 Then ExitFor")
                CR1X_file.writelines("\n      Next")
                CR1X_file.writelines("\n      TwC=Twg_7")
                CR1X_file.writelines("\n      TwF=1.8*TwC+32")
            # LI200X
            CR1X_file.writelines("\n\n  'LI200X Pyranometer measurement")
            CR1X_file.writelines("\n  If solar_exist = 1")
            CR1X_file.writelines("\n    VoltDiff (Solar_w,1,mV200,3,True,0,60,1,0)")
            CR1X_file.writelines("\n    If Solar_w<0 Then Solar_w=0")
            CR1X_file.writelines("\n    Solar_w=Solar_w*200")
            CR1X_file.writelines("\n  Else")
            CR1X_file.writelines("\n    Solar_w=\"NAN\"")
            CR1X_file.writelines("\n  EndIf")
            # TE525
            CR1X_file.writelines("\n\n  'TE525 Tipping Bucket Rain Gauge")
            CR1X_file.writelines("\n  If TE525_exist = 1")
            CR1X_file.writelines("\n    PulseCount (Rain,1,P2,1,0,.01,0)")
            CR1X_file.writelines("\n  Else")
            CR1X_file.writelines("\n    Rain=\"NAN\"")
            CR1X_file.writelines("\n  EndIf")
            # Call Tables
            CR1X_file.writelines("\n\n  'Call Output Tables")
            CR1X_file.writelines("\n  CallTable MesoAtmo")
            CR1X_file.writelines("\n  CallTable MesoRoad")
            CR1X_file.writelines("\n  CallTable Daily")
            CR1X_file.writelines("\n  CallTable TwoMinute")
            if self.CS125 == 1:
                CR1X_file.writelines("\n  CallTable PresentWx")
            CR1X_file.writelines("\n\nNextScan")

            # 5-Second Section (IceSight)
            if self.RS == "IceSight":
                CR1X_file.writelines("\n\nSlowSequence")
                CR1X_file.writelines("\n\nScan (10,Sec,0,0)")
                CR1X_file.writelines("\n  'IceSight non-invasive sensor")
                CR1X_file.writelines("\n  poll=\"AD\"+CHR(13)+CHR(10)'DB")
                CR1X_file.writelines("\n\n  'polled sensor")
                CR1X_file.writelines("\n  SerialOpen(ComC5,9600,0,0,110,4)'DB")
                CR1X_file.writelines("\n  SerialOut (ComC5,poll,\"\",0,100)'DB")
                CR1X_file.writelines("\n  Delay (1,300,mSec)'DB")
                CR1X_file.writelines("\n  SerialInBlock (ComC5,icein,110)'DB")
                CR1X_file.writelines("\n  identifier=Mid (icein,1,2)'DB")
                CR1X_file.writelines("\n  If identifier=\"AR\" Then'DB")
                CR1X_file.writelines("\n    Call parseice485 'DB")
                CR1X_file.writelines("\n    SerialClose (ComC5)")
                CR1X_file.writelines("\n    TwFC=0")
                CR1X_file.writelines("\n    identifier=\" \"")
                CR1X_file.writelines("\n  EndIf")
                CR1X_file.writelines("\n\nNextScan")

            # 10-Second Section (HygroVUE, SR-50, DSC/DST, CS125)
            if self.Snow== "SR50" or self.Snow== "SnowVue" or self.RS == "Vaisala" or self.CS125 == 1 or self.temp == "HygroVUE5/10":
                CR1X_file.writelines("\n\nSlowSequence")
                CR1X_file.writelines("\n\nScan (10,Sec,0,0)")
                # HygroVUE
                if self.temp == "HygroVue5/10":
                    CR1X_file.writelines("\n\n  'HygroVUE")
                    CR1X_file.writelines("\n  SDI12Recorder(TRHData(),C3,\"0\",\"M!\",1,0)")
                    CR1X_file.writelines("\n  Air_Temp_f = AirTC*1.8 + 32")
                    CR1X_file.writelines("\n  RH_percent = RH")
                    CR1X_file.writelines("\n  'WetBulbCalc for HygroVUE5/10")
                    CR1X_file.writelines("\n  AirTC_9=(5/9)*(Air_Temp_f-32)")
                    CR1X_file.writelines("\n  SPkPa_6=101.325")
                    CR1X_file.writelines("\n  SatVP(SVp_11,AirTC_9)")
                    CR1X_file.writelines("\n  Vp_10=RH_percent*SVp_11/100")
                    CR1X_file.writelines("\n  'Dew Point calculation TdF")
                    CR1X_file.writelines("\n  DewPoint(TdC,AirTC_9,RH_percent)")
                    CR1X_file.writelines("\n  If TdC>AirTC_9 OR TdC=NAN Then TdC=AirTC_9")
                    CR1X_file.writelines("\n  TdF=1.8*TdC+32")
                    CR1X_file.writelines("\n  'Find Wet-Bulb TwF")
                    CR1X_file.writelines("\n  Top_14=AirTC_9")
                    CR1X_file.writelines("\n  Bottom_15=TdC")
                    CR1X_file.writelines("\n  For N_17 = 1 To 25")
                    CR1X_file.writelines("\n    Twpg_8=Twg_7")
                    CR1X_file.writelines("\n    Twg_7=((Top_14-Bottom_15)/2)+Bottom_15")
                    CR1X_file.writelines("\n    WetDryBulb(Vpg_9,AirTC_9,Twg_7,SPkPa_6)")
                    CR1X_file.writelines("\n    VpgVpd_13=Vpg_9-Vp_10")
                    CR1X_file.writelines("\n    Twch_12=ABS(Twpg_8-Twg_7)")
                    CR1X_file.writelines("\n    If VpgVpd_13>0 Then")
                    CR1X_file.writelines("\n      Top_14=Twg_7")
                    CR1X_file.writelines("\n    Else")
                    CR1X_file.writelines("\n      Bottom_15=Twg_7")
                    CR1X_file.writelines("\n    EndIf")
                    CR1X_file.writelines("\n    If Twch_12<0.01 OR N_17=25 Then ExitFor")
                    CR1X_file.writelines("\n      Next")
                    CR1X_file.writelines("\n      TwC=Twg_7")
                    CR1X_file.writelines("\n      TwF=1.8*TwC+32")
                # SR50A
                if self.Snow== "SR50":
                    CR1X_file.writelines("\n\n  'Call SR50A Snow Depth Sensor")
                    CR1X_file.writelines("\n  Call SR50A")
                elif self.Snow== "SnowVue":
                    CR1X_file.writelines("\n\n  'Call SnowVue Snow Depth Sensor")
                    CR1X_file.writelines("\n  Call SnowVue")
                else:
                    CR1X_file.writelines("\n\n  Snow_Depth_in = \"NAN\"")
                # DSC/DST
                if self.RS == "Vaisala":
                    CR1X_file.writelines("\n\n  'DSC/DST Stuff")
                    CR1X_file.writelines(
                        "\n  dscpoll = CHR(13)+CHR(64)+CHR(55)+CHR(32)+CHR(77)+CHR(32)+CHR(49)+CHR(54)+CHR(13)  'Carrage return@7 M 16Carrage return")
                    CR1X_file.writelines("\n  'filter definitions")
                    CR1X_file.writelines("\n  dstairtempfilter=CHR(13)+CHR(10)+CHR(48)+CHR(49)  'return linefeed 0 1")
                    CR1X_file.writelines("\n  dstrhfilter=CHR(59)+CHR(48)+CHR(50)               ';02")
                    CR1X_file.writelines("\n  dstdewpointfilter=CHR(59)+CHR(48)+CHR(51)         ';03")
                    CR1X_file.writelines("\n  dstinputvoltfilter=CHR(59)+CHR(49)+CHR(52)        ';14")
                    CR1X_file.writelines("\n  dstsurfacetempfilter=CHR(59)+CHR(54)+CHR(48)      ';60")
                    CR1X_file.writelines("\n  dsthardwarestatusfilter=CHR(59)+CHR(54)+CHR(49)   ';61")
                    CR1X_file.writelines("\n  dscsurfstatusfilter=CHR(59)+CHR(54)+CHR(54)       ';66")
                    CR1X_file.writelines("\n  dsclevelofgripfilter=CHR(59)+CHR(54)+CHR(56)      ';68")
                    CR1X_file.writelines("\n  dschardwarestatusfilter=CHR(59)+CHR(13)+CHR(10)+CHR(55)+CHR(49)   ';71")
                    CR1X_file.writelines("\n  dscamtofwaterfilter=CHR(59)+CHR(55)+CHR(50)       ';72")
                    CR1X_file.writelines("\n  dscamtoficefilter=CHR(59)+CHR(55)+CHR(51)         ';73")
                    CR1X_file.writelines("\n  dscamtofsnowfilter=CHR(59)+CHR(55)+CHR(52)        ';74")
                    # Com type is direct connection  to logger
                    if self.RS_com == 0:
                        CR1X_file.writelines("\n\n  'DSC/DST instructions")
                        CR1X_file.writelines("\n  'opens the serial port")
                        CR1X_file.writelines("\n  SerialOpen (COMC5,9600,0,0,230,4)")
                        CR1X_file.writelines("\n  'send the poll command")
                        CR1X_file.writelines("\n  SerialOut (ComC5,dscpoll,\"\",0,90)")
                        CR1X_file.writelines("\n  'delay prior to measurement")
                        CR1X_file.writelines("\n  Delay (1,200,mSec)")
                        CR1X_file.writelines("\n  'retrieve the data")
                        CR1X_file.writelines("\n  SerialInBlock (ComC5,dscraw,227)")
                        CR1X_file.writelines("\n  SerialClose (ComC5)")
                        CR1X_file.writelines("\n\n  Call DSCparse")
                        CR1X_file.writelines("\n  Call DSCconvert")
                        CR1X_file.writelines("\n  Call DSCOnOff")
                    # Com type is Radio
                    elif self.RS_com == 1:
                        CR1X_file.writelines("\n\n  'DSC/DST instructions")
                        CR1X_file.writelines("\n  'opens the serial port")
                        CR1X_file.writelines("\n  SerialOpen (COMSDC7,9600,0,0,245)")
                        CR1X_file.writelines("\n  'send the poll command")
                        CR1X_file.writelines("\n  SerialOut (ComSDC7,dscpoll,\"\",0,90)")
                        CR1X_file.writelines("\n  'delay prior to measurement")
                        CR1X_file.writelines("\n  Delay (1,400,mSec)")
                        CR1X_file.writelines("\n  'retrieve the data")
                        CR1X_file.writelines("\n  SerialInBlock (ComSDC7,dscraw,227)")
                        CR1X_file.writelines("\n  SerialClose (ComSDC7)")
                        CR1X_file.writelines("\n  dsccheck = Left(dscraw,2)")
                        CR1X_file.writelines('\n  If dsccheck = "07" Then'
                                             '\n    Call DSCparse '
                                             '\n    Call DSCconvert'
                                             '\n  EndIf'
                                             '\n  Call DSCOnOff')

                # CS125
                if self.CS125 == 1:
                    CR1X_file.writelines("\n\n  'CS125 Stuff")
                    CR1X_file.writelines("\n  'Setup datalogger port for binary communication")
                    CR1X_file.writelines("\n  SerialOpen(COMC1,38400,3,0,1000)")
                    CR1X_file.writelines("\n  TempString = \"POLL:0:0\"")
                    CR1X_file.writelines("\n  CheckVal = CheckSum (TempString,1,0)")
                    CR1X_file.writelines(
                        "\n  OutString = CHR(2) + TempString + \":\" + FormatLong (CheckVal,\"%04X\") + \":\" + CHR(3)+ CHR(13) + CHR(10)")
                    CR1X_file.writelines("\n  'Send get data command to cs125, then pause for 1 second")
                    CR1X_file.writelines("\n  SerialOut (COMC1,OutString,\"\",0,100)")
                    CR1X_file.writelines("\n  Delay (1,1,Sec)")
                    CR1X_file.writelines("\n  'Set up COMC1 to receive incoming serial data.")
                    CR1X_file.writelines("\n  SerialInRecord (ComC1,CS125_In,&h02,0,&H03,NBytesReturned,01)")
                    CR1X_file.writelines("\n  'Split out visibility parameters from string input")
                    if self.temp == "CS215-in-CS125":
                        CR1X_file.writelines("\n  SplitStr (cs125out(),CS125_In,\" \",27,5)")
                    else:
                        CR1X_file.writelines("\n  SplitStr (cs125out(),CS125_In,\" \",25,5)")
                    CR1X_file.writelines("\n  visibility_m = vis_m_string")
                    CR1X_file.writelines("\n  visibility_m = visibility_m*2.19")
                    CR1X_file.writelines("\n  visibility_mi = visibility_m*0.000621371192")
                    CR1X_file.writelines("\n\n  If visibility_mi > 10 Then")
                    CR1X_file.writelines("\n    visibility_mi = 10")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  If visibility_mi < 0.01 Then")
                    CR1X_file.writelines("\n    visibility_mi=\"NAN\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines(
                        "\n\n  If Intensity_mm_hr >= 0.3 OR SYNOPCode=51 OR SYNOPCode=61 OR SYNOPCode=71 OR SYNOPCode=72 Then")
                    CR1X_file.writelines("\n    Precip=\"Yes\"")
                    CR1X_file.writelines("\n    If Intensity_mm_hr <3 Then")
                    CR1X_file.writelines("\n      Precip_Intensity=\"Light\"")
                    CR1X_file.writelines("\n    ElseIf Intensity_mm_hr >= 10 Then")
                    CR1X_file.writelines("\n      Precip_Intensity=\"Heavy\"")
                    CR1X_file.writelines("\n    Else")
                    CR1X_file.writelines("\n      Precip_Intensity=\"Moderate\"")
                    CR1X_file.writelines("\n    EndIf")
                    CR1X_file.writelines("\n  Else")
                    CR1X_file.writelines("\n    Precip=\"No\"")
                    CR1X_file.writelines("\n    Precip_Intensity=\" \"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  If CS125_In=\"NAN\" Then")
                    CR1X_file.writelines("\n    Precip=\" \"")
                    CR1X_file.writelines("\n    Precip_Intensity=\" \"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  If visibility_mi < 0.5 AND Precip=\"No\" Then")
                    CR1X_file.writelines("\n    Precip_Intensity = \"Fog\"")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  'Determine snowfall rate")
                    CR1X_file.writelines("\n  If Precip=\"Yes\" AND TwF < 34 AND visibility_mi < 10 Then")
                    CR1X_file.writelines("\n    SnowfallRate = 0.5 / visibility_mi")
                    CR1X_file.writelines("\n    If visibility_mi < 0.25 AND Particle_count <= 200 Then")
                    CR1X_file.writelines("\n      SnowfallRate = 2")
                    CR1X_file.writelines("\n    'ElseIf visibility_mi < 2 AND Particle_count <=50 Then")
                    CR1X_file.writelines("\n    '  SnowfallRate = 0")
                    CR1X_file.writelines("\n    '  Precip=\"No\"")
                    CR1X_file.writelines("\n    '  Precip_Intensity=\"Fog\"")
                    CR1X_file.writelines("\n    ElseIf SnowfallRate >= 5")
                    CR1X_file.writelines("\n      SnowfallRate = 5")
                    CR1X_file.writelines("\n    EndIf")
                    CR1X_file.writelines("\n  Else")
                    CR1X_file.writelines("\n    SnowfallRate = 0")
                    CR1X_file.writelines("\n  EndIF")
                    CR1X_file.writelines("\n\n  If visibility_mi=\"NAN\" Then")
                    CR1X_file.writelines("\n    SnowfallRate = 0")
                    CR1X_file.writelines("\n  EndIf")
                    CR1X_file.writelines("\n\n  'Clear out COMC1 serial buffer")
                    CR1X_file.writelines("\n  SerialFlush (ComC1)")
                    CR1X_file.writelines("\n  SerialClose (ComC1)")
                else:
                    CR1X_file.writelines("\n\n  'No CS125")
                    CR1X_file.writelines("\n  'NAN Variables")
                    CR1X_file.writelines("\n    visibility_mi = \"NAN\"")
                    CR1X_file.writelines("\n    SnowfallRate = \"NAN\"")
                CR1X_file.writelines("\n\nNextScan")

            # 1-Minute Section (light)
            if self.light == 1:
                CR1X_file.writelines("\n\nSlowSequence")
                CR1X_file.writelines("\n\nScan (1,Min,0,0)")
                CR1X_file.writelines("\n\n  If Solar_w = 0 AND Batt_volt > 12")
                CR1X_file.writelines("\n    SW12 (SW12_1,1)")
                CR1X_file.writelines("\n    Light=\"On\"")
                CR1X_file.writelines("\n  Else")
                CR1X_file.writelines("\n    SW12 (SW12_1,0)")
                CR1X_file.writelines("\n    Light=\"Off\"")
                CR1X_file.writelines("\n  EndIf")
                CR1X_file.writelines("\n\nNextScan")

            # 5-Minute Section (soil moisture)
            if self.CS655 == 1:
                CR1X_file.writelines("\n\nSlowSequence")
                CR1X_file.writelines("\n\nScan (5,Min,0,0)")
                CR1X_file.writelines("\n  SDI12Recorder (CS655(),C3,\"0\", \"M3!\",1,0)")
                CR1X_file.writelines("\n  T=T*1.8+32")
                CR1X_file.writelines("\n  CallTable SoilMoisture")
                CR1X_file.writelines("\n\nNextScan")

            CR1X_file.writelines("\nEndProg\n")
            CR1X_file.close()

        # BEGIN WRITING CR1000 PROGRAM-----------------------------------------------------------------------------------------
        if self.logger_type == "CR1000":
            filename = "{0}_{1}_Auto.CR1".format(self.site_name, self.date)
            CR1_file = open(self.path + filename, "w")

            # HEADER INFO--------------------
            CR1_file.writelines(
                ["'CR1000 program automatically generated by RWISPrograms.py on ", month, "/", day, "/", year, " for ",
                 self.site_name, " \n"])
            CR1_file.writelines(["'Generator: ", self.username, " \n"])
            CR1_file.writelines("\n")
            CR1_file.writelines("'Instruments included: \n")

            CR1_file.writelines("\nEndProg\n")
            CR1_file.close()

        # BEGIN WRITING CR300 PROGRAM------------------------------------------------------------------------------------------
        if self.logger_type == "CR3XX":
            filename = "{0}_{1}_Auto.CR300".format(self.site_name, self.date)
            CR300_file = open(self.path + filename, "w")

            # HEADER INFO------------------
            CR300_file.writelines(
                ["'CR300 program automatically generated by RWISPrograms.py on ", month, "/", day, "/", year, " for ",
                 self.site_name, " \n"])
            CR300_file.writelines(["'Generator: ", self.username, " \n"])
            CR300_file.writelines("\n")
            CR300_file.writelines("'Instruments included: \n")
            CR300_file.writelines("'Legacy thermometer (HMP45, Rotronic, EE181)")
            if self.wind == "Regular":
                CR300_file.writelines(", 05103 or Legacy Alpine Anemometer")
            else:
                CR300_file.writelines(", HD or HD Alpine Anemometer")
            if self.subprobe == "107" or self.subprobe == "108":
                CR300_file.writelines([", ", str(self.subprobe)])
            CR300_file.writelines("\n'Output Data Tables: MesoAtmo, MesoRoad, Daily")

            # DECLARE PUBLIC VARIABLES----------------------------------------
            CR300_file.writelines("\n\n'Declare Public Variables")
            CR300_file.writelines("\nPublic Batt_volt")
            CR300_file.writelines("\nPublic Air_Temp_f")
            CR300_file.writelines("\nPublic RH_percent")
            CR300_file.writelines("\nPublic TdC")
            CR300_file.writelines("\nPublic TwC")
            CR300_file.writelines("\nPublic TdF")
            CR300_file.writelines("\nPublic TwF")
            CR300_file.writelines("\nPublic Wind_Speed_mph")
            CR300_file.writelines("\nPublic Wind_Dir_deg")
            CR300_file.writelines("\nPublic Two_Min_Wind_Dir_deg")
            CR300_file.writelines("\nPublic Two_Min_Wind_Speed_mph")
            CR300_file.writelines("\nPublic Ground_18in_Temp_f")

            # DECLARE PRIVATE VARIABLES-------------------------
            CR300_file.writelines("\n\n'Declare Private Variables")
            CR300_file.writelines("\nDim AirTC_9")
            CR300_file.writelines("\nDim SPkPa_6")
            CR300_file.writelines("\nDim Twg_7")
            CR300_file.writelines("\nDim Twpg_8")
            CR300_file.writelines("\nDim Vpg_9")
            CR300_file.writelines("\nDim Vp_10")
            CR300_file.writelines("\nDim SVp_11")
            CR300_file.writelines("\nDim Twch_12")
            CR300_file.writelines("\nDim VpgVpd_13")
            CR300_file.writelines("\nDim Top_14")
            CR300_file.writelines("\nDim Bottom_15")
            CR300_file.writelines("\nDim N_17")

            # DEFINE UNITS---------------------
            CR300_file.writelines("\n\n'Define Units")
            CR300_file.writelines("\nUnits Batt_volt=Volts")
            CR300_file.writelines("\nUnits Air_Temp_f=Deg F")
            CR300_file.writelines("\nUnits RH_percent=%")
            CR300_file.writelines("\nUnits TdF=Deg F")
            CR300_file.writelines("\nUnits TwF=Deg F")
            CR300_file.writelines("\nUnits Wind_Speed_mph=miles/hour")
            CR300_file.writelines("\nUnits Wind_Dir_deg=degrees")
            CR300_file.writelines("\nUnits Ground_18in_Temp_f=Deg F")

            # DEFINE DATA TABLES-------------------------------------
            # MesoAtmo Table
            CR300_file.writelines("\n\n'Define Data Tables")
            CR300_file.writelines("\n'MesoAtmo table")
            CR300_file.writelines("\nDataTable (MesoAtmo,1,1008)")
            CR300_file.writelines("\n  DataInterval (0,10,min,10)")
            CR300_file.writelines("\n  Sample (1,Air_Temp_f,FP2)")
            CR300_file.writelines("\n  Sample (1,RH_percent,FP2)")
            CR300_file.writelines("\n  Sample (1,Two_Min_Wind_Dir_deg,FP2)")
            CR300_file.writelines("\n  Sample (1,Two_Min_Wind_Speed_mph,FP2)")
            CR300_file.writelines("\n  Maximum (1,Wind_Speed_mph,FP2,False,True)")
            CR300_file.writelines("\n  Sample(1,Batt_volt,FP2)")
            CR300_file.writelines("\n  Sample(1,TdF,FP2)")
            CR300_file.writelines("\n  Sample(1,TwF,FP2)")
            CR300_file.writelines("\nEndTable")

            # MesoRoad Table
            CR300_file.writelines("\n\n'MesoRoad table")
            CR300_file.writelines("\nDataTable (MesoRoad,1,1008)")
            CR300_file.writelines("\n  DataInterval (0,10,min,10)")
            CR300_file.writelines("\n  Sample(1,Ground_18in_Temp_f,FP2)")
            CR300_file.writelines("\nEndTable")

            # Daily Table
            CR300_file.writelines("\n\n'Daily table")
            CR300_file.writelines("\nDataTable (Daily,1,-1)")
            CR300_file.writelines("\n  DataInterval (0,1440,min,10)")
            CR300_file.writelines("\n  Minimum(1,Batt_Volt,FP2,False,True)")
            CR300_file.writelines("\n  Maximum(1,Air_Temp_f,FP2,False,True)")
            CR300_file.writelines("\n  Minimum(1,Air_Temp_f,FP2,False,True)")
            CR300_file.writelines("\n  Maximum(1,RH_percent,FP2,False,True)")
            CR300_file.writelines("\n  Minimum(1,RH_percent,FP2,False,True)")
            CR300_file.writelines("\n  Maximum(1,TdF,FP2,False,True)")
            CR300_file.writelines("\n  Minimum(1,TdF,FP2,False,True)")
            CR300_file.writelines("\n  Maximum(1,TwF,FP2,False,True)")
            CR300_file.writelines("\n  Minimum(1,TwF,FP2,False,True)")
            CR300_file.writelines("\n  Average(1,Wind_Speed_mph,FP2,False)")
            CR300_file.writelines("\n  Maximum(1,Wind_Speed_mph,FP2,False,True)")
            CR300_file.writelines("\n  Average(1,Ground_18in_Temp_f,FP2,False)")
            CR300_file.writelines("\nEndTable")

            # TwoMinute Table
            CR300_file.writelines("\n\n'TwoMinute table (for wind)")
            CR300_file.writelines("\nDataTable (TwoMinute,1,-1)")
            CR300_file.writelines("\n  DataInterval (0,120,sec,10)")
            CR300_file.writelines("\n  WindVector (1,Wind_Speed_mph,Wind_Dir_deg,FP2,False,0,0,1)")
            CR300_file.writelines("\nEndTable\n")

            # MAIN PROGRAM-----------------------
            CR300_file.writelines("\n'Main Program")
            CR300_file.writelines("\nBeginProg")

            # 1-Second Section
            CR300_file.writelines("\nScan (1,Sec,0,0)")
            # Battery Voltage
            CR300_file.writelines("\n\n  Battery (Batt_volt)")
            # Anemometer
            if self.wind == "Regular":
                CR300_file.writelines("\n\n  '(Regular) Wind Speed & Direction Sensor measurements WS_ms and Wind_Dir_Deg:")
                CR300_file.writelines("\n  PulseCount(Wind_Speed_mph,1,P_LL,1,1,0.2192,0)")
            else:
                CR300_file.writelines("\n\n  '(HD) Wind Speed & Direction Sensor measurements WS_ms and Wind_Dir_Deg:")
                CR300_file.writelines("\n  PulseCount(Wind_Speed_mph,1,P_LL,1,1,0.3726,0)")
            CR300_file.writelines("\n  BrHalf(Wind_Dir_deg,1,mV2500,3,VX1,1,2500,False,20000,60,355,0)")
            CR300_file.writelines("\n  If Wind_Dir_deg>=355 Then Wind_Dir_deg=0")
            CR300_file.writelines("\n  'Pull two minute values from the two minute table")
            CR300_file.writelines("\n  Two_Min_Wind_Speed_mph=TwoMinute.Wind_Speed_mph_WVc(1)")
            CR300_file.writelines("\n  Two_Min_Wind_Dir_deg=TwoMinute.Wind_Speed_mph_WVc(2)")
            # Subprobe
            if self.subprobe == "107":
                CR300_file.writelines("\n\n  '107 - Sub Temperature Probe measurement 18in_Ground_Temp_F:")
                CR300_file.writelines("\n  Therm107(Ground_18in_Temp_f,1,4,VX1,0,60,1.8,32)")
            elif self.subprobe == "108":
                CR300_file.writelines("\n\n  '108 - Sub Temperature Probe measurement 18in_Ground_Temp_F:")
                CR300_file.writelines("\n  Therm108(Ground_18in_Temp_f,1,4,VX1,0,60,1.8,32)")
            else:
                CR300_file.writelines("\n\n  'No subprobe:")
                CR300_file.writelines("\n  Ground_18in_Temp_f = \"NAN\"")
            # Legacy Thermometers
            CR300_file.writelines(
                "\n\n  'Rotronic, EE181, or HMP45C Temp/RH Sensor Measurements Air_Temp_f and RH_Percent:")
            CR300_file.writelines("\n  VoltSe(Air_Temp_f,1,mV2500,1,False,0,60,0.18,-40)")
            CR300_file.writelines("\n  VoltSE(RH_percent,1,mV2500,2,False,0,60,0.1,0)")
            CR300_file.writelines("\n  If RH_percent>100 Then RH_percent=100")
            CR300_file.writelines("\n  'Dew Point and Wet-Bulb Calculation Prep")
            CR300_file.writelines("\n  AirTC_9=(5/9)*(Air_Temp_f-32)")
            CR300_file.writelines("\n  SPkPa_6=101.325")
            CR300_file.writelines("\n  SatVP(SVp_11,AirTC_9)")
            CR300_file.writelines("\n  Vp_10=RH_percent*SVp_11/100")
            CR300_file.writelines("\n  'Dew Point calculation TdF")
            CR300_file.writelines("\n  DewPoint(TdC,AirTC_9,RH_percent)")
            CR300_file.writelines("\n  If TdC>AirTC_9 OR TdC=NAN Then TdC=AirTC_9")
            CR300_file.writelines("\n  TdF=1.8*TdC+32")
            CR300_file.writelines("\n  'Find Wet-Bulb TwF")
            CR300_file.writelines("\n  Top_14=AirTC_9")
            CR300_file.writelines("\n  Bottom_15=TdC")
            CR300_file.writelines("\n  For N_17 = 1 To 25")
            CR300_file.writelines("\n    Twpg_8=Twg_7")
            CR300_file.writelines("\n    Twg_7=((Top_14-Bottom_15)/2)+Bottom_15")
            CR300_file.writelines("\n    WetDryBulb(Vpg_9,AirTC_9,Twg_7,SPkPa_6)")
            CR300_file.writelines("\n    VpgVpd_13=Vpg_9-Vp_10")
            CR300_file.writelines("\n    Twch_12=ABS(Twpg_8-Twg_7)")
            CR300_file.writelines("\n    If VpgVpd_13>0 Then")
            CR300_file.writelines("\n    	Top_14=Twg_7")
            CR300_file.writelines("\n    Else")
            CR300_file.writelines("\n    	Bottom_15=Twg_7")
            CR300_file.writelines("\n    EndIf")
            CR300_file.writelines("\n    If Twch_12<0.01 OR N_17=25 Then ExitFor")
            CR300_file.writelines("\n      Next")
            CR300_file.writelines("\n      TwC=Twg_7")
            CR300_file.writelines("\n      TwF=1.8*TwC+32")

            # Call Tables
            CR300_file.writelines("\n\n  'Call Output Tables")
            CR300_file.writelines("\n  CallTable MesoAtmo")
            CR300_file.writelines("\n  CallTable MesoRoad")
            CR300_file.writelines("\n  CallTable Daily")
            CR300_file.writelines("\n  CallTable TwoMinute")

            CR300_file.writelines("\n\nNextScan")
            CR300_file.writelines("\nEndProg\n")
            CR300_file.close()

################################ Driver Code ################################
if __name__ == "__main__":
    sGui = StationGui()
    sGui.validate()

