import time, math
from machine import UART
from lsm9ds1 import LSM9DS1
from machine import Pin, I2C
uart = UART(0,baudrate=9600)


def score(input):
    if input[1] <= -1.8999338150024414:
        var0 = [1.0, 0.0, 0.0, 0.0, 0.0]
    else:
        if input[4] <= 0.7034878134727478:
            if input[5] <= -0.4954542815685272:
                if input[1] <= 1.1435582637786865:
                    if input[0] <= -0.9549519717693329:
                        if input[4] <= 0.14280001819133759:
                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
                    else:
                        if input[8] <= 0.16107146441936493:
                            if input[8] <= -0.5036864876747131:
                                if input[1] <= 0.3902007266879082:
                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                if input[0] <= 2.896871328353882:
                                    if input[4] <= -1.6795920729637146:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        if input[1] <= 0.8720047175884247:
                                            if input[8] <= -0.42519623041152954:
                                                if input[1] <= 0.36723634600639343:
                                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                else:
                                                    var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                            else:
                                                if input[8] <= 0.15569089353084564:
                                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                else:
                                                    if input[0] <= -0.0028863251209259033:
                                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                    else:
                                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            if input[0] <= 0.8767518401145935:
                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                else:
                    if input[0] <= -0.06354073621332645:
                        if input[3] <= -0.22321168333292007:
                            var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                        else:
                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                    else:
                        if input[3] <= 0.3503490388393402:
                            if input[5] <= -0.5901323854923248:
                                if input[5] <= -1.6537352204322815:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                            else:
                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            if input[7] <= -0.40345972776412964:
                                if input[8] <= -0.05025830492377281:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                            else:
                                if input[5] <= -1.2738555073738098:
                                    if input[7] <= 0.4007618576288223:
                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
            else:
                if input[5] <= 0.2886899262666702:
                    if input[1] <= 0.5652956962585449:
                        if input[0] <= -0.26632897555828094:
                            if input[4] <= 0.15000208839774132:
                                if input[1] <= 0.5358395576477051:
                                    if input[0] <= -0.3599499464035034:
                                        if input[1] <= 0.48967576026916504:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                        else:
                                            if input[7] <= -0.5358298122882843:
                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        if input[6] <= -0.4053550660610199:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                        else:
                                            if input[8] <= -0.4099991023540497:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                else:
                                    if input[7] <= -0.16868556290864944:
                                        if input[1] <= 0.5593844652175903:
                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                if input[0] <= -0.8272497057914734:
                                    var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
                                else:
                                    if input[8] <= -0.25981151312589645:
                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            if input[7] <= 0.2829221114516258:
                                if input[8] <= -0.4215756207704544:
                                    var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                else:
                                    if input[5] <= 0.21246741712093353:
                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                    else:
                        if input[0] <= 0.7669868171215057:
                            if input[7] <= -0.3642376959323883:
                                if input[1] <= 1.0191293358802795:
                                    if input[0] <= -1.6340214610099792:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        if input[8] <= -0.09522414952516556:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                        else:
                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                else:
                                    if input[8] <= -0.06073777098208666:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                            else:
                                if input[2] <= 1.735123872756958:
                                    if input[0] <= -1.1898861825466156:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        if input[3] <= -2.1206281185150146:
                                            if input[2] <= -0.47226832807064056:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                        else:
                                            if input[4] <= -1.5417951345443726:
                                                if input[8] <= -0.3335559666156769:
                                                    var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                                else:
                                                    if input[1] <= 0.7895059585571289:
                                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                    else:
                                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                            else:
                                                if input[3] <= -1.6461980938911438:
                                                    if input[3] <= -1.8192769289016724:
                                                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                                    else:
                                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                else:
                                                    if input[4] <= -0.8644758760929108:
                                                        if input[0] <= -0.11469728872179985:
                                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                        else:
                                                            var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                                    else:
                                                        if input[5] <= -0.4788542538881302:
                                                            if input[3] <= 0.00015484541654586792:
                                                                var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                                            else:
                                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                        else:
                                                            var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                else:
                                    if input[8] <= 0.018269766122102737:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                        else:
                            if input[8] <= -0.046678610146045685:
                                if input[0] <= 0.8446046710014343:
                                    if input[3] <= -0.1899908185005188:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                else:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                if input[8] <= 0.14852242916822433:
                                    if input[7] <= 0.1194063238799572:
                                        if input[2] <= 2.1581974625587463:
                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    if input[4] <= -1.240640252828598:
                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                else:
                    if input[8] <= 0.5281916856765747:
                        if input[4] <= 0.5675353109836578:
                            if input[5] <= 0.34931421279907227:
                                if input[0] <= 0.39333122968673706:
                                    if input[4] <= 0.35374288260936737:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
                                else:
                                    if input[0] <= 0.6160922348499298:
                                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                    else:
                                        if input[7] <= -0.669842541217804:
                                            if input[8] <= -0.05517790140584111:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            if input[0] <= 0.6724192202091217:
                                                var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                if input[3] <= 2.032349705696106:
                                    if input[4] <= 0.4384026378393173:
                                        if input[5] <= 0.3714563846588135:
                                            if input[5] <= 0.37137024104595184:
                                                if input[6] <= 0.43041151762008667:
                                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                else:
                                                    if input[6] <= 0.4904750734567642:
                                                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                                    else:
                                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                                        else:
                                            if input[0] <= 4.651864290237427:
                                                if input[3] <= 1.2339706420898438:
                                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                else:
                                                    if input[3] <= 1.2349128127098083:
                                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                    else:
                                                        if input[5] <= 0.5524535477161407:
                                                            if input[5] <= 0.5466190874576569:
                                                                if input[8] <= 0.09332631900906563:
                                                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                                else:
                                                                    if input[2] <= 0.0984867662191391:
                                                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                                    else:
                                                                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                            else:
                                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                        else:
                                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                if input[0] <= 4.657325506210327:
                                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                                else:
                                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        if input[0] <= -1.2081413865089417:
                                            var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
                                        else:
                                            if input[7] <= -0.7327759563922882:
                                                if input[6] <= -0.23498165234923363:
                                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                                else:
                                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    if input[8] <= 0.17884103953838348:
                                        if input[8] <= 0.13697945326566696:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                        else:
                                            if input[2] <= -0.6984298974275589:
                                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                            else:
                                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                    else:
                                        if input[6] <= 0.733150064945221:
                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            if input[0] <= -0.16430288553237915:
                                var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
                            else:
                                if input[5] <= 2.4710729122161865:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                    else:
                        if input[5] <= 1.0283377915620804:
                            var0 = [0.0, 0.0, 0.0, 1.0, 0.0]
                        else:
                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
        else:
            if input[0] <= -0.6591287292540073:
                var0 = [0.0, 0.0, 0.0, 0.0, 1.0]
            else:
                if input[1] <= 0.2768670469522476:
                    if input[3] <= -2.831993818283081:
                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                    else:
                        var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                else:
                    if input[8] <= -0.22874180227518082:
                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                    else:
                        if input[1] <= 1.6733772158622742:
                            if input[2] <= -0.633153572678566:
                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                if input[7] <= -1.4556301832199097:
                                    var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                else:
                                    if input[7] <= 0.0012377724051475525:
                                        if input[8] <= 0.15624886378645897:
                                            var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
                                        else:
                                            var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                                    else:
                                        var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                        else:
                            if input[5] <= 2.237245202064514:
                                var0 = [0.0, 0.0, 1.0, 0.0, 0.0]
                            else:
                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0]
    return var0


class SensorDataProcessor:
    # Changed aggregation method from sum to average
    method_names = ['average']
    max_length = 10

    def __init__(self, prefix):
        self.buffer = []
        self.prefix_name = prefix
        
    def add_data(self, new_data):
        if len(self.buffer) == self.max_length:
            self.buffer.pop(0)
        self.buffer.append(new_data)
    
    def average(self, buffer):
        return float(sum(buffer)) / len(buffer)
    
    def calculate_all(self, new_data):
        self.add_data(new_data)
        if len(self.buffer) < self.max_length:
            return None  # Not enough data yet
        results = []
        results.extend(self.buffer)
        for method_name in self.method_names:
            method = getattr(self, method_name)
            results.append(method(self.buffer))
        return results

# Initialize the sensor (IMU) and I2C bus.
i2c = I2C(1, scl=Pin(15), sda=Pin(14))
imu = LSM9DS1(i2c)

# Create SensorDataProcessor objects for accelerometer, gyroscope, and magnetometer axes.
# Accelerometer processors
acc_x_obj = SensorDataProcessor(prefix="ax_")
acc_y_obj = SensorDataProcessor(prefix="ay_")
acc_z_obj = SensorDataProcessor(prefix="az_")

# Gyroscope processors
gyro_x_obj = SensorDataProcessor(prefix="gx_")
gyro_y_obj = SensorDataProcessor(prefix="gy_")
gyro_z_obj = SensorDataProcessor(prefix="gz_")

# Magnetometer processors
mag_x_obj = SensorDataProcessor(prefix="mx_")
mag_y_obj = SensorDataProcessor(prefix="my_")
mag_z_obj = SensorDataProcessor(prefix="mz_")

activity_labels = {
    0: "W",
    1: "I",
    2: "I",
    3: "W",
    4: "I"
}

while True:
    # Get raw sensor data.
    ax, ay, az = imu.accel()
    gx, gy, gz = imu.gyro()
    mx, my, mz = imu.magnet()
    
    # Print raw sensor data for debugging.
    #print("Accel:", ax, ay, az)
    #print("Gyro:", gx, gy, gz)
    #print("Mag:", mx, my, mz)
    
    # Process each reading.
    ax_result = acc_x_obj.calculate_all(ax)
    ay_result = acc_y_obj.calculate_all(ay)
    az_result = acc_z_obj.calculate_all(az)
    
    gx_result = gyro_x_obj.calculate_all(gx)
    gy_result = gyro_y_obj.calculate_all(gy)
    gz_result = gyro_z_obj.calculate_all(gz)
    
    mx_result = mag_x_obj.calculate_all(mx)
    my_result = mag_y_obj.calculate_all(my)
    mz_result = mag_z_obj.calculate_all(mz)
    
    # Proceed only when all sensor buffers are full.
    if (ax_result is not None and ay_result is not None and az_result is not None and
        gx_result is not None and gy_result is not None and gz_result is not None and
        mx_result is not None and my_result is not None and mz_result is not None):
        
        feature_vector = (ax_result + ay_result + az_result +
                          gx_result + gy_result + gz_result +
                          mx_result + my_result + mz_result)
        
        # Ensure the feature vector has 100 elements.
        while len(feature_vector) < 100:
            feature_vector.append(0.0)
        
        # Print the feature vector for debugging.
        #print("Feature vector:", feature_vector)
        
        prediction_result = score(feature_vector)
        max_accuracy = max(prediction_result)
        max_index = prediction_result.index(max_accuracy)
        
        print("Detected Activity:", activity_labels[max_index])
        uart.write(activity_labels[max_index] + '\n')  # Add newline for easier parsing on receiving end
        #time.sleep(0.15)
        


        
    
    
    time.sleep(0.1)



   

