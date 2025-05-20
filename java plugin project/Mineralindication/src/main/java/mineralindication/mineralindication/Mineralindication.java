package mineralindication.mineralindication;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Random;

public final class Mineralindication extends JavaPlugin {

    private static Mineralindication main;
    public static Mineralindication getPlugin() {
        return new Mineralindication();
    }
    public static Mineralindication getMain(){
        return main;
    }

    public boolean contains(String cyber) {
        return false;
    }

    @Override
    public void onEnable() {
        main = this;
        Random random = new Random();
        main.saveDefaultConfig();
        System.out.println("started");
        String ip = main.getConfig().getString("SQL.ip");
        String table = main.getConfig().getString("SQL.table");
        String individual = main.getConfig().getString("SQL.individual SQL base");
        String user = main.getConfig().getString("SQL.user");
        String password = main.getConfig().getString("SQL.password");
        String DB_DRIVER = "com.mysql.jdbc.Driver";
        String DB_URL = "jdbc:mysql://"+ ip + "/" +table;
        String DB_IND = "jdbc:mysql://"+ ip + "/" +individual;
        String DB_USERNAME = user;
        String DB_PASSWORD = password;
        Connection conn = null;
        try{
            //Register the JDBC driver
            Class.forName(DB_DRIVER);
            //Open the connection
            conn = DriverManager.
                    getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            if(conn != null){
                System.out.println("Successfully connected.");
            }else{
                System.out.println("Failed to connect.");
            }
        }catch(Exception e){
            e.printStackTrace();
        }
        getCommand("register").setExecutor(new register());
        getCommand("token").setExecutor(new takemineral());
        Bukkit.getServer().getPluginManager().registerEvents(new mineralshow(), this);
        try(Connection connn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            Statement stmt = connn.createStatement();
            Statement stmt2 = connn.createStatement();
            Statement stmt3 = connn.createStatement();
            Statement stmt4 = connn.createStatement();
            Statement stmt5 = connn.createStatement();
            Statement stmt6 = connn.createStatement();
        ) {
            String mineral = "CREATE TABLE mineral " +
                    "(id INTEGER not NULL, " +
                    " iron INTEGER, " +
                    " coal INTEGER, " +
                    " diamond INTEGER, " +
                    " copper INTEGER, " +
                    " redstone INTEGER, " +
                    " gold INTEGER, " +
                    " emerald INTEGER, " +
                    " PRIMARY KEY ( id ), "+
                    " CHECK(copper >= 0), " +
                    " CHECK(iron >= 0), " +
                    " CHECK(redstone >= 0), " +
                    " CHECK(coal >= 0), " +
                    " CHECK(gold >= 0), " +
                    " CHECK(diamond >= 0), " +
                    " CHECK(emerald >= 0)) ";
            String usermineral = "CREATE TABLE usermineral " +
                    "(id INTEGER not NULL, " +
                    " UUID VARCHAR(255), " +
                    " username VARCHAR(255), " +
                    " password VARCHAR(255), " +
                    " money VARCHAR(255), " +
                    " iron INTEGER, " +
                    " coal INTEGER, " +
                    " diamond INTEGER, " +
                    " copper INTEGER, " +
                    " redstone INTEGER, " +
                    " gold INTEGER, " +
                    " emerald INTEGER, " +
                    " PRIMARY KEY ( id )," +
                    " CHECK(money >= 0), " +
                    " CHECK(copper >= 0), " +
                    " CHECK(iron >= 0), " +
                    " CHECK(redstone >= 0), " +
                    " CHECK(coal >= 0), " +
                    " CHECK(gold >= 0), " +
                    " CHECK(diamond >= 0), " +
                    " CHECK(emerald >= 0), " +
                    " CHECK(money >= 0)) ";
            String takemineral = "CREATE TABLE takemineral " +
                    "(id VARCHAR(255) not NULL, " +
                    " UUID VARCHAR(255), " +
                    " token VARCHAR(255), " +
                    " iron INTEGER, " +
                    " coal INTEGER, " +
                    " diamond INTEGER, " +
                    " copper INTEGER, " +
                    " redstone INTEGER, " +
                    " gold INTEGER, " +
                    " emerald INTEGER, " +
                    " PRIMARY KEY ( id ), "+
                    " CHECK(copper >= 0), " +
                    " CHECK(iron >= 0), " +
                    " CHECK(redstone >= 0), " +
                    " CHECK(coal >= 0), " +
                    " CHECK(gold >= 0), " +
                    " CHECK(diamond >= 0), " +
                    " CHECK(emerald >= 0)) ";
            stmt.executeUpdate(mineral);
            stmt2.executeUpdate(usermineral);
            stmt3.executeUpdate(takemineral);
            System.out.println("Created table in given database...");
            String mineralrow = "INSERT INTO mineral VALUES (0, 1, 1, 1, 1, 1, 1, 1)";
            stmt4.executeUpdate(mineralrow);
            String usermineralrow = "INSERT INTO usermineral VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)";
            stmt5.executeUpdate(usermineralrow);
            String takerow = "INSERT INTO takemineral VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)";
            stmt6.executeUpdate(takerow);
        } catch (SQLException e) {
            e.printStackTrace();
        } }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
